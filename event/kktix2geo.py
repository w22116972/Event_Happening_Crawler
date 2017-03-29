import ast
import json

import googlemaps

for line in open('api_key.txt').readlines():
    API_KEY = line


def geocode(address):
    '''
    Return tuple of longitude and latitude
    '''
    # Geocoding an address
    gmaps = googlemaps.Client(key=API_KEY)
    geocode_result = gmaps.geocode(address)
    lst = []
    for i in geocode_result:
        lst.append(repr(i['geometry']['location']['lng'])+ ',' + repr(i['geometry']['location']['lat']))
    return lst


with open('./kktix_geo.csv', 'w') as f:
    for line in open('./kktix.csv').readlines():
        field = line.split(',')[0]
        if field != 'address':
            geo = geocode(field)
            if len(geo) > 0:
                lng = geo[0].split(',')[0]
                lat = geo[0].split(',')[1]
                f.write(line.replace('\n', '') + ',' + lng + ',' + lat + '\n')
            else:
                continue
        else:
            f.write(line.replace('\n', '') + ',lng,lat\n')
    f.close()