from django.shortcuts import render, get_object_or_404, get_list_or_404
from django import forms
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.http import *
from django.views.decorators.csrf import csrf_exempt
from django.utils import simplejson
import socket

from chatUs.models import Event, ChatLOG
from utils.geo import getLatFromStrPoint, getLonFromStrPoint

from chatUs.models import Event
from utils.geo import getLatFromStrPoint, getLonFromStrPoint, appendToLog
from chatUs import Util_DB
# Create your views here.

@csrf_exempt
def input_message(request):
    uName = ""
    timeText = ""
    textToSend = ""
    
    print request.POST
    
    if request.POST.has_key("userName"):
        uName = request.POST["userName"]
    if request.POST.has_key("time"):
        timeText = request.POST["time"]
    if request.POST.has_key("text"):
        textToSend = request.POST["text"]
    
    #If there a name then a new message has been posted
    if uName:
        chatlog = ChatLOG(Event='1', User=uName, Text=textToSend, DateTime=timeText)
        chatlog.save()
    #Otherwise it is considered a request for the newest
    #data, based on the timeText which will instead
    #represent the time in since 1/1/1970
    
    
    return HttpResponse("{'text':'salut!'}", mimetype="application/json")

class LoginForm(forms.Form):
    """
    Class specifiant un formulaire pour ce loguer
    """
    username = forms.CharField()

class CreateEventForm(forms.Form):
    Name = forms.CharField()
    StartDate = forms.DateField()
    EndDate = forms.DateField()
    StartTime = forms.TimeField()
    EndTime = forms.TimeField()
    Cost = forms.DecimalField()
    Phone = forms.CharField()
    Email = forms.CharField()
    Description = forms.CharField()
    City = forms.CharField()
    Adress = forms.CharField()

def login(request):
    """
    Fonction idantifiant les gens et/ou renvoyant le formulaire.
    """
    message = None
    form = None
    if request.method == 'POST':

        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            form = LoginForm(request.POST) 
            if form.is_valid(): 
                request.session['username'] = form.cleaned_data['username']
            
        else:
            message = "Please enable cookies and try again."
    else:
        form = LoginForm()

    request.session.set_test_cookie()
    if(request.session['username']):
        topThree = Util_DB.GetSortedEventList(request.session['latitude'],request.session['longitude'])[0:3]
    else:
        topThree = Util_DB.GetSortedEventList(request.session['latitude'],request.session['longitude'])[0:3]
        
    return render_to_response('index.html',
                              {
                                'form': form,
                                'message':message,
                                "topThree" : topThree,
                              },
                              context_instance = RequestContext(request))

def event(request, event_id):
    appendToLog( 'event: ')
    event = get_object_or_404(Event, id=event_id)
    topThree = []
    if request.session.has_key('latitude') and request.session.has_key('longitude'):
        topThree = Util_DB.GetSortedEventList(request.session['latitude'],request.session['longitude'])[0:3]
    
    
    
    
    return render_to_response('event.html',
        {
        "event" : event,
        "topThree" : topThree,
        },
          context_instance = RequestContext(request) )           
    
    
    

def event_list(request):
    

    print request
    
    event_list = []
    if request.session.has_key('latitude') and request.session.has_key('longitude'):
        event_list = Util_DB.GetSortedEventList(request.session['latitude'],request.session['longitude'])
    topThree = event_list[0:3]
    
    return render_to_response('eventList.html',
        {
        "events" : event_list,
        "topThree" : topThree,
        },
          context_instance = RequestContext(request) )


def create_event(request):
    topThree = []
    if request.session.has_key('latitude') and request.session.has_key('longitude'):
        topThree = Util_DB.GetSortedEventList(request.session['latitude'],request.session['longitude'])[0:3]
    if request.method == 'POST': # If the form has been submitted...
        form = CreateEventForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            
            print request.POST
            if request.POST['ville'].tolower() == "sherbrooke":
                
                
                DjanCity, fuckOff = City.objects.get_or_create(Name = "Sherbrooke")
                DjanEvent = Event(
                                  Name = request.POST['titre'],
                                  StartDate = request.POST['dateDebut'],
                                  EndDate = request.POST['dateFin'],
                                  StartTime = request.POST['heureDebut'],
                                  EndTime = request.POST['heureFin'],
                                  Cost = request.POST['cout'],
                                  Phone = request.POST['telephone'],
                                  Email = request.POST['email'],
                                  Description = request.POST['descript'],
                                  Adress = request.POST['address'],
                                  Latitude = getLatFromStrPoint(request.POST['address']),
                                  Longitude = getLonFromStrPoint(request.POST['address'])
                                  )
                DjanEvent.save()
                
            # Process the data in form.cleaned_data
            # ...
           # return HttpResponseRedirect('/thanks/') # Redirect after POST
        else:
            form = CreateEventForm() # An unbound form
    
    return render_to_response('createEvent.html',
        {
        'form': form,
        "topThree" : topThree,
        },
          context_instance = RequestContext(request) )

@csrf_exempt
def receive_coord(request):
    request.session['latitude'] = request.POST['x']
    request.session['longitude'] = request.POST['y']

    return  HttpResponse()