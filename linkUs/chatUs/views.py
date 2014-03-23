from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from chatUs.models import Event
from utils.geo import getLatFromStrPoint, getLonFromStrPoint
# Create your views here.

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
    
    return render_to_response('index.html',
                              {
                                'form': form,
                                'message':message,
                              },
                              context_instance = RequestContext(request))

def event(id,request):
     return render(request, 'event.html', {
          "event" : event.getObject_or_404(),
      })

def event_list(request):
    return render(request, 'eventList.html', {})

def create_event(request):
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

    return render(request, 'createEvent.html', {
        'form': form,
    })

@csrf_exempt
def receive_coord(request):
    request.session['latitude'] = request.POST['x']
    request.session['longitude'] = request.POST['y']

    return  HttpResponse()