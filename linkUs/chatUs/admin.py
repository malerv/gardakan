from django.contrib import admin
from .models import ChatLOG

# Register your models here.

class ChatLOGAdmin(admin.ModelAdmin):
    pass


admin.site.register(ChatLOG, ChatLOGAdmin)