import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import folium


key = "6d6f969fd9024ac8afde957f0c86a5ba"

num = input("Enter your phone number with country code: ")

ch_num = phonenumbers.parse(num,'CH')
num_location = geocoder.description_for_number(ch_num, "en")
print(num_location)

serviceName = phonenumbers.parse(num, 'RO')
print(carrier.name_for_number(serviceName, 'en'))


from opencage.geocoder import OpenCageGeocode

geocod = OpenCageGeocode(key)

query = str(num_location)
results = geocod.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

mapLocation = folium.Map(location = [lat,lng], zoom_start = 2)
folium.Marker([lat,lng], popup=num_location).add_to(mapLocation)
mapLocation.save("NumberLocation.html")
