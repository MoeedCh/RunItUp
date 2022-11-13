# Going to hold all the locally stored data in this current Runtime
from googlemaps import distance_matrix
from googlemaps import Client
from BackEnd import retrieve_info
from Interface import Locations

def withInRadius(location1 : tuple, location2: tuple, radius: int) -> bool:
    gmaps = Client(key="AIzaSyA-BRYsxwC4d1mNlFOwwjJtaQI9HGLm5u0")
    distance = distance_matrix.distance_matrix(origins = location1, destinations = location2, client=gmaps, units='imperial')
    if distance['rows'][0]['elements'][0]['status'] != "ZERO_RESULTS":

        miles = distance['rows'][0]['elements'][0]["distance"]['text']
        miles = float(miles[:len(miles)-2].replace(",", ""))
        if miles <= radius:
            return True
    return False



class PopulateGmap:

    def __init__(self, location: tuple, radius=30):
        self.locationsOnMap = []
        self.userLocation = location
        self.allLocations = retrieve_info.getAllLocations()
        self.radius = radius
        self.getAllLocationsNearUser()


    def getAllLocationsNearUser(self):
        for location in self.allLocations:
            place = Locations.Locations(name=location["name"], address=location["address"], latitude=location['geolocation'][0], longitude=location['geolocation'][1], fields={})
            if withInRadius(self.userLocation, place.getLocation(), self.radius):
                self.locationsOnMap.append(place)


    def getLocationsFilter(self, fieldType):
        locations = retrieve_info.getLocationInfo({'fields': fieldType})

        for location in locations:
            place = Locations.Locations(name=location["name"], address=location["address"], latitude=location['geolocation'][0], longitude=location['geolocation'][1], fields={})
            if withInRadius(self.userLocation, place.getLocation(), self.radius):
                self.locationsOnMap.append(place)

