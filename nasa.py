import requests
import json
from datetime import datetime, timedelta
import pandas as pd

date = datetime.today()
API_KEY = "cKHzDHu797xhVuCX2Z25x38Qj6ZAtlowWg8DnXYP"
URL_APOD = "https://api.nasa.gov/planetary/apod?api_key={}".format(API_KEY)
URL_NEOWS = "https://api.nasa.gov/neo/rest/v1/feed?start_date={}&end_date={}&api_key={}".format(str(date-timedelta(days = 7)).split()[0],str(date).split()[0],API_KEY)


def get_nasa_apod():
    response = requests.get(URL_APOD)
    return response.json()

def get_nasa_neows():
    response = requests.get(URL_NEOWS)
    return response.json()

def make_neows_dataframe():
    data = get_nasa_neows()
    bodies = []
    for date in data['near_earth_objects']:
        for i in range(len(data['near_earth_objects'][date])):
            bodies.append([date,data['near_earth_objects'][date][i]['name'],data['near_earth_objects'][date][i]['estimated_diameter']['meters']['estimated_diameter_max'],data['near_earth_objects'][date][i]['close_approach_data'][0]['miss_distance']['kilometers'],data['near_earth_objects'][date][i]['close_approach_data'][0]['relative_velocity']['kilometers_per_hour'],data['near_earth_objects'][date][i]['close_approach_data'][0]['orbiting_body'],data['near_earth_objects'][date][i]['is_potentially_hazardous_asteroid']])
    df = pd.DataFrame(bodies,columns = ['Date','Name','Diameter','Miss_distance','Velocity','Orbiting_body','Hazardous'])
    return df
    
def get_hazardous_proportion(data):
    return data[data['Hazardous'] == True].shape[0]/data.shape[0]


if __name__ == "__main__":
    datita = make_neows_dataframe()
    print(datita.head(10))
   