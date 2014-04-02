from django.contrib import admin
from .models import ChatLOG, Event

# Register your models here.

class ChatLOGAdmin(admin.ModelAdmin):
    pass

class EventAdmin(admin.ModelAdmin):
    pass

admin.site.register(ChatLOG, ChatLOGAdmin)
admin.site.register(Event, EventAdmin)
