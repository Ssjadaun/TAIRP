import phonenumbers
import opencage
import folium
from myNumber import number

from phonenumbers import geocoder
salNumber = phonenumbers.parse(number)
Location = geocoder.description_for_number(salNumber,'en')
print(Location)

# service provider
from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,'en'))

from opencage.geocoder import OpenCageGeocode
key = '8a27ffb676654ef58a535960a313e24c'
geocoder = OpenCageGeocode(key)
query = str(Location)
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(Location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=Location).add_to(myMap)

myMap.save('myLocation.html')


