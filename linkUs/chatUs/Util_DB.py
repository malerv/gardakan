'''
Created on Mar 22, 2014

@author: Vincent
'''

import json
from chatUS.models import Event

def AddEvents(events):
    for event in events:
        DjanEvent = Event(
                          Name=event['TITRE'],
                          Description=event['DESCRIP'],
                          ImagePath=event['URL_PHOTO'],
                          DateTime=event['DT01'],
                          Category=event['CATEG'],
                          Adress=event['AD'],
                          Latitude=TODO_GetLatitude(event['GEOM']),
                          Longitude=TODO_GetLongitude(event['GEOM']))
        
        DjanEvent.save()
    
    


def AddLibraryEvents():
    json_data=open('../../DonneeOuverte/SherbrookeLibraryEvents.json')
    data = json.loads(json_data)
    addEvents(data)
        
    

def AddHockeyEvents():
    json_data=open('../../DonneeOuverte/SherbrookeHockeyEvents.json')
    data = json.loads(json_data)
    addEvents(data)
       
       
def AddPoolEvents():  
    json_data=open('../../DonneeOuverte/SherbrookePoolEvents.json')
    data = json.loads(json_data)
    addEvents(data)
    
def AddSherbrookeEvents():
    json_data=open('../../DonneeOuverte/SherbrookeEvents.json')
    data = json.loads(json_data)
    addEvents(data)
     

def FillDB():
    AddLibraryEvents()
    AddHockeyEvents()
    AddPoolEvents()
    AddSherbrookeEvents()

    
    
    
