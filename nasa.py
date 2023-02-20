import requests
import json
from datetime import datetime, timedelta
import pandas as pd

date = datetime.today()
API_KEY = "cKHzDHu797xhVuCX2Z25x38Qj6ZAtlowWg8DnXYP"
URL_APOD = "https://api.nasa.gov/planetary/apod?api_key={}".format(API_KEY)
URL_NEOWS = "https://api.nasa.gov/neo/rest/v1/feed?start_date={}&end_date={}&api_key={}".format(str(date-timedelta(days = 7)).split()[0],str(date).split()[0],API_KEY)
URL_MARS = "https://api.nasa.gov/insight_weather/?api_key={}&feedtype=json&ver=1.0".format(API_KEY)


def get_data(url):
    response = requests.get(url)
    return response.json()

def make_neows_dataframe(data):
    bodies = []
    for date in data['near_earth_objects']:
        for i in range(len(data['near_earth_objects'][date])):
            bodies.append([date,data['near_earth_objects'][date][i]['name'],float(data['near_earth_objects'][date][i]['estimated_diameter']['meters']['estimated_diameter_max']),float(data['near_earth_objects'][date][i]['close_approach_data'][0]['miss_distance']['kilometers']),float(data['near_earth_objects'][date][i]['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']),data['near_earth_objects'][date][i]['close_approach_data'][0]['orbiting_body'],data['near_earth_objects'][date][i]['is_potentially_hazardous_asteroid']])
    df = pd.DataFrame(bodies,columns = ['Date','Name','Diameter','Miss_distance','Velocity','Orbiting_body','Hazardous'])
    return df

def get_hazardous_proportion(data):
    return data[data['Hazardous'] == True].shape[0]/data.shape[0]

def get_mars_weather():
    response = requests.get(URL_MARS)
    return response.json()



    
   