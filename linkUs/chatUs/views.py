from django.shortcuts import render
from django import forms
# Create your views here.

class LoginForm(forms.Form):
    username = forms.CharField()

def login(request):

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