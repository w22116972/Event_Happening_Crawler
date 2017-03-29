import ast
import json

import googlemaps

# API_KEY = 'AIzaSyAnp9UZ7Zg8XtT1S71kNjNc3T-ScOGBXAA'
API_KEY = 'AIzaSyAbIBwJeeMz58TdawmXWk0-WwBONlDwYyI'
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

with open('2017_buy_geo.csv', 'w') as f:
    for line in open('2017_buy.csv').readlines():
        addr = line.split(',')[2]
        if addr != '土地區段位置或建物區門牌':
            if '臺北市' not in addr:
                addr = '臺北市' + addr
            geo = geocode(addr)
            if len(geo) > 0:
                lng = geo[0].split(',')[0]
                lat = geo[0].split(',')[1]
                f.write(line.replace('\n', '') + ',' + lng + ',' + lat + '\n')
            else:
                continue
        else:
            f.write(line.replace('\n', '') + ',lng,lat\n')
    f.close()