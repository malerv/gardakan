import math
import requests


def getLatFromStrPoint(strPoint):
    strPoint = strPoint.split("(")[1]
    return float(strPoint.split(",")[0])

def getLonFromStrPoint(strPoint):
    strPoint = strPoint.split("(")[1]
    strPoint = strPoint.split(",")[1]
    return float(strPoint.split(")")[0])

def getDistanceBetween(lat1, long1, lat2, long2):

    # Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
    radOfEarth = 6371000
        
    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
        
    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
        
    # Compute spherical distance from spherical coordinates.
        
    # For two locations in spherical coordinates 
    # (1, theta, phi) and (1, theta, phi)
    # cosine( arc length ) = 
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length
    
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos(cos)

    # Remember to multiply arc by the radius of the earth 
    # in your favorite set of units to get length.
    return arc*radOfEarth

def getLatLonFromAddr(adress):
    lat = 0.0
    lng = 0.0
    urlTest = 'https://maps.googleapis.com/maps/api/geocode/json?address'
    first = True
    for txt in adress.split(" "):
        if first == True:
            urlTest+='='
            first = False
        else:
            urlTest+='+'
        urlTest+=txt
    urlTest+='&sensor=false'
    r=requests.get(urlTest)
    data = r.json()
    if data['status']=="OK":
        lat = data['results'][0]['geometry']['location']['lat']
        lng = data['results'][0]['geometry']['location']['lng']

    return [lat,lng]