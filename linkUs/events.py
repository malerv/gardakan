from django.shortcuts import get_object_or_404
from django.utils.html import strip_tags
from django_socketio import events
import sys

@events.on_message
def message(request, socket, context, message):
    socket.send(message)
    
@events.on_connect
def connected(request, socket, context):
    print("connected")
    