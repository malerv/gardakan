from django.shortcuts import render
from django import forms
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
    if request.method == 'POST': # If the form has been submitted...
        form = LoginForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            #TODO check si c'est valide et unique en ce moment.
            pass
    else:
        form = LoginForm() # An unbound form

    return render(request, 'index.html', {
        'form': form,
    })


def event(request):
    return render(request, 'event.html', {})

def event_list(request):
    return render(request, 'eventList.html', {})

def create_event(request):
    return render(request, 'createEvent.html', {})