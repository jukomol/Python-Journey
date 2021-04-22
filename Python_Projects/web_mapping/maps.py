import pandas as pd
import geopy
from geopy.geocoders import Nominatim
data = pd.read_csv("map.txt")
nom = Nominatim()
countries=data['Country']


with open("hello"+".txt", 'w') as file:
    for i in countries:
        n= nom.geocode(countries[0])
        file.write(str(n.latitude)+"\n")
