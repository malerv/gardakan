from django.db import models

# Create your models here.
class Event(models.Model):
    Name = models.CharField(max_length=255)
    Subtitle = models.CharField(max_length=255)
    Description = models.CharField(max_length=1024)
    Information = models.CharField(max_length=1024)
    DateTime = models.DateTimeField()
    Category = models.CharField(max_length=255)
    Adress = models.CharField(max_length=255)
    Latitude = models.DecimalField(max_digits=19, decimal_places=16)
    Longitude = models.DecimalField(max_digits=19, decimal_places=16)
    
    City = models.ForeignKey('City')
    

class RecurrentEvent(models.Model):
    Name = models.CharField(max_length=255)
    Subtitle = models.CharField(max_length=255)
    Description = models.CharField(max_length=1024)
    Information = models.CharField(max_length=1024)
    WeekDay = models.CharField(max_length=255)
    Category = models.CharField(max_length=255)
    CivicAdress = models.CharField(max_length=255)
    StreetName = models.CharField(max_length=255)
    Latitude = models.DecimalField(max_digits=19, decimal_places=16)
    Longitude = models.DecimalField(max_digits=19, decimal_places=16)
    City = models.ForeignKey('City')
    
    
    

class City(models.Model):
    Name = models.CharField(max_length=255)
    MunID = models.CharField(max_length=255)
        
class ChatLOG(models.Model):
    Event = models.ForeignKey(Event)
    User = models.CharField(max_length=255)
    Text = models.CharField(max_length=255)
    DateTime = models.DateTimeField()
    
        
        
        
        
        