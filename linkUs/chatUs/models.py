from django.db import models

# Create your models here.
class Event(models.Model):
    Name = models.CharField(max_length=255)
    Subtitle = models.CharField(max_length=255)
    Description = models.CharField(max_length=1024)
    Information = models.CharField(max_length=1024)
    ImagePath = models.ImageField()
    DateTime = models.DateTimeField()
    Category = models.CharField(max_length=255)
    Adress = models.CharField(max_length=255)
    Latitude = models.DecimalField()
    Longitude = models.DecimalField()
    
    City = models.ForeignKey(City)
    

class RecurrentEvent(models.Model):
    Name = models.CharField(max_length=255)
    Subtitle = models.CharField(max_length=255)
    Description = models.CharField(max_length=1024)
    Information = models.CharField(max_length=1024)
    ImagePath = models.ImageField()
    WeekDay = models.CharField(max_length=255)
    Category = models.CharField(max_length=255)
    CivicAdress = models.CharField(max_length=255)
    StreetName = models.CharField(max_length=255)
    Latitude = models.DecimalField()
    Longitude = models.DecimalField()
    City = models.ForeignKey(City)
    
    
    

class City(models.Model):
    Name = models.CharField(max_length=255)
    Latitude = models.DecimalField()
    Longitude = models.DecimalField()
        
class ChatLOG(models.Model):
    Event = models.ForeignKey(Event)
    User = models.CharField(max_length=255)
    Text = models.CharField(max_length=255)
    DateTime = models.DateTimeField()
    
        
        
        
        
        