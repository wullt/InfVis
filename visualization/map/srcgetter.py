import pandas as pd
import json

def getU5MR(year):
    df = pd.read_csv("with_decrease_percent_since_1975.csv")
    return df.loc[df['Year'] == year]

def getGeoJson():
    f=open("custom.geo.json","r")
    geojson = json.loads(f.read())
    f.close()
    return geojson