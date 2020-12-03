
import plotly.express as px
import srcgetter
df = srcgetter.getU5MR(1980)

import plotly.io as pio
pio.kaleido.scope.default_width = 500
pio.kaleido.scope.default_height = 400

print(df)

country_codes_len3 = []
for index, row in df.iterrows():
    ctycode = str(row["CountryCode"])
    if(len(ctycode) == 3):
        country_codes_len3.append(ctycode)
    if(len(ctycode) == 2):
        country_codes_len3.append("0"+ctycode)
    if(len(ctycode) == 1):
        country_codes_len3.append("00"+ctycode)

df["CountryCode"] = country_codes_len3


geojson = srcgetter.getGeoJson()



colors=["#fef0d9","#fdd49e","#fdbb84","#fc8d59","#ef6548","#d7301f","#990000"]

cs7=[
    [0,colors[0]],[1/6,colors[0]],
    [1/6,colors[1]],[1/3,colors[1]],
    [1/3,colors[2]],[0.5,colors[2]],
    [0.5,colors[3]],[2/3,colors[3]],
    [2/3,colors[4]],[5/6,colors[4]],
    [5/6,colors[5]],[0.999,colors[5]],
    [0.999,colors[6]],[1,colors[6]],
]


fig = px.choropleth(df, geojson=geojson, color="Value",
                    color_continuous_scale=cs7,
                    range_color=[0,300],
                   

                    locations="CountryCode", featureidkey="properties.iso_n3",hover_name="Country",
                    projection="mercator"
                    )
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0},showlegend=False)

fig.write_image("export/map1.png")
fig.show()
