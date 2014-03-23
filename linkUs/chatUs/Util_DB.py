'''
Created on Mar 22, 2014

@author: Vincent
'''

import json
import math
from pprint import pprint
from chatUs.models import Event, City
from utils.geo  import  getLatFromStrPoint, getLonFromStrPoint

#from utils  import geo
from operator import itemgetter


def AddEvents(events):
    
    for event in events:
        pprint(event)
        
        DjanCity, fuckOff = City.objects.get_or_create(Name="Sherbrooke",MunID=event['MUNID'])
        
        
        
        if event.get('AD') == None:
            Ad = "PAS_DADRESSE"
           # Ad = TODO_GetPointFromAdress( MUN + LOC)
        else:
            Ad = event['AD']
        

        
        if event.get('GEOM') == None:
            Lat = 0
            Lon = 0
            #TODO_GetPointFromAdress
        else:
            Lat = getLatFromStrPoint(event['GEOM'])
            Lon = getLonFromStrPoint(event['GEOM'])
            
            
        
        
        DjanEvent = Event(
                          Name=event['TITRE'],
                          Description=event['DESCRIP'],
                          DateTime=event['DT01'],
                          Category=event['CATEG'],
                          Adress=Ad,
                          Latitude=Lat,
                          Longitude=Lon,
                          City = DjanCity )
        
        DjanEvent.save()
    
    


def AddLibraryEvents():
    json_data=open('../DonneeOuverte/SherbrookeLibraryEvents.json')
    data = json.load(json_data)
    AddEvents(data)
        
    

def AddHockeyEvents():
    json_data=open('../DonneeOuverte/SherbrookeHockeyEvents.json')
    data = json.load(json_data)
    AddEvents(data)
       
       
def AddPoolEvents():  
    json_data=open('../DonneeOuverte/SherbrookePoolEvents.json')
    data = json.load(json_data)
    AddEvents(data)
    
def AddSherbrookeEvents():
    json_data=open('../DonneeOuverte/SherbrookeEvents.json')
    data = json.load(json_data)
    AddEvents(data['EVTS']['EVT'])
     

def FillDB():
    print "DEBUT"
    AddSherbrookeEvents()
   # AddLibraryEvents()
   # AddHockeyEvents()
   # AddPoolEvents()
    print "FIN"
    
    
def GetSortedEventList(UserLat,UserLon):
    DjanEvents = Event.objects.all()
    array = []
    
    for DjanEvent in DjanEvents:
        dist = getDistanceBetween(DjanEvent.Latitude, DjanEvent.Longitude, UserLat, UserLon)
        array.append([DjanEvent,dist])
        
    SortedList = sorted(array, key=itemgetter(1))
    
    return SortedList
    
    
    
def main():
    # my code here
    print "Main"
    #FillDB()
    GetSortedEventList(5,5)
    
main()

    
    
    
