from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class LoginForm(forms.Form):
    """
    Class specifiant un formulaire pour ce loguer
    """
    username = forms.CharField()


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

def event(request):
    return render(request, 'event.html', {})

def event_list(request):
    return render(request, 'eventList.html', {})

def create_event(request):
    return render(request, 'createEvent.html', {})

@csrf_exempt
def receive_coord(request):
    request.session['latitude'] = request.POST['x']
    request.session['longitude'] = request.POST['y']

    return  HttpResponse()