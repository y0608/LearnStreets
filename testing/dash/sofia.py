import plotly.express as px

df = px.data.election()
geojson = px.data.election_geojson()

fig = px.choropleth_mapbox(df, geojson=geojson, color="winner",
                           locations="district", featureidkey="properties.district",
                           center={"lat": 42.698334, "lon": 23.319941}, zoom=12)

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

fig.show()
