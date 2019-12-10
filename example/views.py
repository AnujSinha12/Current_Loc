from django.shortcuts import render
import requests
import folium
from django.http import HttpResponse

def home(request):
    print('_________entered home________')
    print('request = ', request)
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    response = requests.get('http://api.ipstack.com/182.71.127.226?access_key=696a5cf8489d7b4901da525454cb3ef2')
    geodata = response.json()

    # geodata = """{'ip': '182.71.127.226', 'type': 'ipv4', 'continent_code': 'AS', 'continent_name': 'Asia',
    #            'country_code': 'IN', 'country_name': 'India', 'region_code': 'DL', 'region_name': 'Delhi',
    #            'city': 'New Delhi', 'zip': '110020', 'latitude': 28.542800903320312, 'longitude': 77.28050231933594, 'location': {'geoname_id': 1261481, 'capital': 'New Delhi', 'languages': [{'code': 'hi', 'name': 'Hindi', 'native': 'हिन्दी'}, {'code': 'en', 'name':'English', 'native': 'English'}], 'country_flag': 'http://assets.ipstack.com/flags/in.svg', 'country_flag_emoji': '��', 'country_flag_emoji_unicode': 'U+1F1EE U+1F1F3', 'calling_code': '91', 'is_eu': False}}"""
    #

    print('geodata = ', geodata)

    ip = geodata['ip']
    country = geodata['country_name']
    latitude = geodata['latitude']
    longitude = geodata['longitude']
    api_key = '696a5cf8489d7b4901da525454cb3ef2'
    continent_name = geodata['continent_name']
    region_name = geodata['region_name']
    city = geodata['city']
    zip = geodata['zip']
    country_flag = geodata['location']['country_flag']
    country_flag_emoji = geodata['location']['country_flag_emoji']

    print('ip = ', ip)
    print("country = ", country)
    print("latitude = ", latitude)
    print("longitude = ", longitude)
    print("api_key = ", api_key)
    print('continent_name = ', continent_name)
    print("region_name = ", region_name)
    print("city = ", city)
    print("zip = ", zip)
    print("country_flag = ", country_flag)
    print("country_flag_emoji = ", country_flag_emoji)

    context = {
            'ip': ip,
            'country': country,
            'latitude': latitude,
            'longitude': longitude,
            'api_key': api_key,
            'continent_name': continent_name,
            'region_name': region_name,
            'city': city,
            'zip': zip,
            'country_flag': country_flag,
            'country_flag_emoji': country_flag_emoji
        }

    # print('response = ', response)

    # ##create map object
    # m = folium.Map(location=[latitude, longitude], zoom_start=20)
    #
    # ##global tooltip
    # tooltip = 'Click for more info'
    #
    # popup = 'IP-{},LATITUDE-{},LONGITUDE-{},COUNTRY-{}, CONTINENT-{}, REGION-{}, CITY-{}, ZIP-{}, COUNTRY_FLAG-{}, EMOJI-{}'.format(ip, latitude, longitude, country, continent_name, region_name, city, zip, country_flag, country_flag_emoji)
    #
    # ##create markers
    # folium.Marker([latitude, longitude], popup=popup, tooltip=tooltip).add_to(m)
    #
    # print('file = ', __file__)
    #
    # ##generate map
    # m.save('example/templates/map.html')

    try:
        return render(request, 'home.html', context)
        #return HttpResponse(request, 'home.html', context)
    except BaseException as msg:
        print('msg = ', msg)

