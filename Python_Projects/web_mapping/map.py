import folium, pandas
data = pandas.read_csv("Volcanoes.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
name = list(data['NAME'])
loca = list(data['LOCATION'])
elev = list(data['ELEV'])

def color_producer(elevation):
    if elevation<1000:
        return 'green'
    elif 1000<=elevation<3000:
        return 'orange';
    else:
        return 'red'


map = folium.Map(location= [38.58, -99.09], zoom_start=6)

fgv = folium.FeatureGroup(name='Volcanoes')

for lt, ln, na, loc, el in zip(lat, lon, name, loca, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=na + ","+ loc, fill_color=color_producer(el), color='grey', fill_opacity=0.7, zoom_start=6))


fgp = folium.FeatureGroup(name='Population')

fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000
else 'orange' if  1000000<= x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map.html")