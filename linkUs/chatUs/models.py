from django.db import models

# Create your models here.
class Event(models.Model):
    Name = models.CharField(max_length=255)
    Subtitle = models.CharField(max_length=255,null=True)
    Description = models.CharField(max_length=1024,null=True)
    Information = models.CharField(max_length=1024,null=True)
    StartDate = models.DateField(null=True)
    EndDate = models.DateField(null=True)
    StartTime = models.TimeField(null=True)
    EndTime = models.TimeField(null=True)
    WeekDay = models.CharField(max_length=255,null=True)
    Category = models.CharField(max_length=255,null=True)
    Adress = models.CharField(max_length=255,null=True)
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
    
        
        
        
        
        