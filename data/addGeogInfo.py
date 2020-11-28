"""
"#region+main+name+preferred": "Asia",
"#region+name+preferred+sub": "Southern Asia",



"""
from hdx.location.country import Country
import pandas as pd

df = pd.read_csv("prepared_data/trimmed_75_2020.csv")

print(df)


regions = []
continents=[]
latitudes=[]
longitudes=[]
for index, row in df.iterrows():
    #print(row['Country or Area Code'], row['Country or Area'])
    region="null"
    continent = "null"
    latitude="null"
    longitude="null"
    try:
        datadict = Country.get_country_info_from_m49(row['Country or Area Code'])
        region=datadict['#region+name+preferred+sub']
        continent=datadict['#region+main+name+preferred']
        latitude=datadict['#geo+lat']
        longitude=datadict['#geo+lon']
    except:
        region= (row['Country or Area']+" is not a Country!")
        print("error at "+row['Country or Area'])
    regions.append(region)
    continents.append(continent)
    latitudes.append(latitude)
    longitudes.append(longitude)
        
df["region"] = regions
df["continent"] = continents
df["latitude"]=latitudes
df["longitude"]=longitudes
df.to_csv("prepared_data/withGeogInfo_75_2020.csv",index=False)