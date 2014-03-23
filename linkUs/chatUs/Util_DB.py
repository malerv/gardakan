'''
Created on Mar 22, 2014

@author: Vincent
'''

import json
import math
from pprint import pprint
from chatUs.models import Event, City
from utils.geo  import  getLatFromStrPoint, getLonFromStrPoint, getDistanceBetween, getLatLonFromAddr

#from utils  import geo
from operator import itemgetter


def AddEvents(events):
    
    for event in events:
        pprint(event)
        
        
        IsOk = True
        tName  = event.get('TITRE')
        tSubtitle = None
        tDescription = event.get('DESCRIP')
        tInformation = None
        tStartDate = event.get('DT01')
        tEndDate = event.get('DT02')
        tStartTime = event.get('HR01')
        tEndTime = event.get('HR02')
        tCategory = event.get('CATEG')
        tAdress = event.get('AD')
        tLocation = event.get('LOC')
        tLatitude = 0
        tLongitude = 0
        tCityName = "Sherbrooke"
        tMunID = event.get('MUNID')
        tGeometry = event.get('GEOM')
        tWeekDay = event.get('JOUR_SEMAINE')
        tCost = event.get('CO')
        tPhone = event.get('TEL1')
        tEmail = event.get('CONTACT')
    
        
        if tAdress == None:
            
            if tLocation != None:
                tAdress = tLocation
            else:
                tAdress = None
       
             
        if tGeometry == None:
        
            if tAdress != None:
                pass
                LatLonArray = getLatLonFromAddr(tAdress)
                tLatitude = LatLonArray[0]
                tLongitude = LatLonArray[1]
                 
            else:
                IsOk = False
                 
        else:
            
            tLatitude = getLatFromStrPoint(tGeometry)
            tLongitude = getLonFromStrPoint(tGeometry)
            
        if IsOk:
        
            DjanCity, fuckOff = City.objects.get_or_create(Name = tCityName, MunID = tMunID)


            DjanEvent = Event(
                              Name = tName,
                              Subtitle = tSubtitle,
                              Description = tDescription,
                              Information = tInformation,
                              StartDate = tStartDate,
                              EndDate = tEndDate,
                              StartTime = tStartTime,
                              EndTime = tEndTime,
                              WeekDay = tWeekDay,
                              Category = tCategory,
                              Adress = tAdress,
                              Latitude = tLatitude,
                              Longitude = tLongitude,
                              Cost = tCost,
                              Phone = tPhone,
                              Email = tEmail,
                              City = DjanCity
                              )
        
            DjanEvent.save()
    
    


def AddLibraryEvents():
    json_data=open('../DonneeOuverte/SherbrookeLibraryEvents.json')
    data = json.load(json_data)
    AddEvents(data['EVTS']['EVT'])
        
    

def AddHockeyEvents():
    json_data=open('../DonneeOuverte/SherbrookeHockeyEvents.json')
    data = json.load(json_data)
    AddEvents(data['PATIN_HOCKEY_LIBRES']['PATIN_HOCKEY_LIBRE'])
       
       
def AddPoolEvents():  
    json_data=open('../DonneeOuverte/SherbrookePoolEvents.json')
    data = json.load(json_data)
    AddEvents(data['EVTS']['EVT'])
    
def AddSherbrookeEvents():
    json_data=open('../DonneeOuverte/SherbrookeEvents.json')
    data = json.load(json_data)
    AddEvents(data['EVTS']['EVT'])
     

def FillDB():
    print "DEBUT"
    #AddSherbrookeEvents()
   # AddLibraryEvents()
   # AddHockeyEvents()
   # AddPoolEvents()
    print "FIN"
    
    

    
def GetSortedEventList(UserLat,UserLon):
    DjanEvents = Event.objects.all()
    array = []
    
    for DjanEvent in DjanEvents:
        
       # print DjanEvent.Latitude
        #print DjanEvent.Longitude
        #print UserLat
        #print UserLon
        
        dist = getDistanceBetween(DjanEvent.Latitude, DjanEvent.Longitude, UserLat, UserLon)
        
        array.append([DjanEvent,int(dist)])
        
    SortedList = sorted(array, key=itemgetter(1))
   # array2 = []
    
    #for item in SortedList:
     #   array2.append(item[0])
      #  print item[0]
    
    return SortedList
    
    
    
def main():
    # my code here
    print "Main"
    FillDB()
    GetSortedEventList(45.399896,-71.884232)
    
main()

    
    
    
