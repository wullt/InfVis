import plotly.graph_objects as go
import pandas as pd
import plotly.io as pio
pio.kaleido.scope.default_width = 2240
pio.kaleido.scope.default_height = 1040

df = pd.read_csv('src/export_trimmed_latlon_cont_renamed.csv')
continents = pd.read_csv('src/export_continent.csv')

#get countries grouped by continents (not used anymore)

europe = df.loc[df['continent'] == "Europe"]
americas = df.loc[df['continent'] == "Americas"]
namerica = df.loc[df['region'] == "Northern America"]
samerica = df.loc[df['region'] == "Latin America and the Caribbean,Americas"]
asia = df.loc[df['continent'] == "Asia"]
africa = df.loc[df['continent'] == "Africa"]
oceania = df.loc[df['continent'] == "Oceania"]


ct_europe = continents.loc[continents["Country"] == "Europe"]
ct_africa = continents.loc[continents["Country"] == "Africa"]
ct_america = continents.loc[continents["Country"] == "Americas"]
ct_namerica = continents.loc[continents["Country"] == "Northern America"]
ct_samerica = continents.loc[continents["Country"] == "South America"]
ct_asia = continents.loc[continents["Country"] == "Asia"]
ct_oceania = continents.loc[continents["Country"] == "Oceania"]


# Highlighted (not used anymore)

cambodia = oceania = df.loc[df['Country'] == "Cambodia"]
rwanda = oceania = df.loc[df['Country'] == "Rwanda"]

world = pd.read_csv('src/export_world.csv')

countries_by_continent = [asia, africa, namerica, europe, samerica, oceania]
continent_total = [ct_asia, ct_africa, ct_namerica,
                   ct_europe, ct_samerica, ct_oceania]

conticolors = ["rgb(255,134,0)",
               "rgb(233,213,0)",
               "rgb(215,2,6)",
               "rgb(0,0,255)",
               "rgb(0,180,0)",
               "rgb(152,0,133)"]




fig = go.Figure()

line_shape = "spline"

marker_80_x = [1980, 1980.5]


marker_200 = [200, 200]
marker_124 = [124, 124]
marker_20_x = [2015, 2020]

year_marker_x = [1980, 2020, 2020, 1980]
year_marker_y = [124, 124, 39, 39]

# Add gray highlights
fig.add_trace(go.Scatter(x=marker_80_x, y=marker_200,
                         mode='lines', line_shape=line_shape, fill="tozeroy",
                         line=dict(color='rgb(196, 196, 196)', width=0, dash='solid')))

fig.add_trace(go.Scatter(x=marker_20_x, y=marker_124,
                         mode='lines', line_shape=line_shape, fill="tozeroy",
                         line=dict(color='rgb(196, 196, 196)', width=0, dash='solid')))

# Add green highlight(global decrease)
fig.add_trace(go.Scatter(x=year_marker_x, y=year_marker_y,
                         mode='lines', line_shape="linear", fill="toself",
                         line=dict(color='rgb(180, 255, 176)', width=0, dash='solid')))

#one line for each country, colorized by continent:
"""
i = 0
for cont in countries_by_continent:
    fig.add_trace(go.Scatter( x=cont.Year, y=cont.Value,
    mode='lines',line_shape="linear",
    line=dict(color=conticolors[i],width=0.25)))
    
    
    i+=1
"""

# add trace for cambodia and rwanda (was not done because the change of the global value looks smaller than it is)
"""
fig.add_trace(go.Scatter( x=cambodia.Year, y=cambodia.Value,
    mode='lines',line_shape="linear",
    line=dict(color=conticolors[0],width=2)))
fig.add_trace(go.Scatter( x=rwanda.Year, y=rwanda.Value,
    mode='lines',line_shape="linear",
    line=dict(color=conticolors[1],width=2)))
"""
# add white bg to the lines -->used when all countries were plottet to increase visibility
"""
for ct in continent_total:
    fig.add_trace(go.Scatter(x=ct.Year, y=ct.Value,
                             mode='lines', line_shape=line_shape, fill='none',
                             line=dict(color='rgba(255,255,255,1)', width=5)))
"""

#plot all continents
i = 0
for ct in continent_total:

    fig.add_trace(go.Scatter(x=ct.Year, y=ct.Value,
                             mode='lines', line_shape=line_shape, fill='none',
                             line=dict(color=conticolors[i], width=3, dash="solid")))

    i += 1
#plot the world avg
fig.add_trace(go.Scatter(x=world.Year, y=world.Value,
                         mode='lines', line_shape="spline",
                         line=dict(color='rgb(0,0,0)', width=4, dash='solid')))



fig.update_layout(
    showlegend=False, # Legend was done independently
    plot_bgcolor='white', 
    xaxis=dict(
        showline=True,
        showgrid=False,

        showticklabels=True,
        #linecolor='rgb(204, 204, 204)',
        linecolor='rgb(0, 0, 0)',
        gridcolor='rgb(0, 0, 0)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=20,
            color='rgb(82, 82, 82)',
        ),

        range=[1980, 2020]
    ),
    yaxis=dict(
        showgrid=True,
        zeroline=True,
        showline=True,
        showticklabels=True,
        linecolor='rgb(0, 0, 0)',
        gridcolor='rgb(200,200, 200)',
        tickfont=dict(
            family='Arial',
            size=20,
            color='rgb(82, 82, 82)',
        ),

        # type='log', ## was used with cambodia and rwanda
        range=[0, 200]  #set range
    ), margin={"r": 0, "t": 0, "l": 0, "b": 0}) #maximize it


fig.write_image("export/linechart_wg.png")

fig.show()
