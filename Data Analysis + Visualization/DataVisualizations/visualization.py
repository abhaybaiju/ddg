import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot

world_happiness_path = "../datasets/world-happiness/"
gapminder_path = "../datasets/gapminder/datasets_5533_8279_gapminder.tsv"

data2015_wh = pd.read_csv(world_happiness_path + "2015.csv")
data2016_wh = pd.read_csv(world_happiness_path + "2016.csv")
data2017_wh = pd.read_csv(world_happiness_path + "2017.csv")
data2018_wh = pd.read_csv(world_happiness_path + "2018.csv")
data2019_wh = pd.read_csv(world_happiness_path + "2019.csv")

data_gm = pd.read_csv(gapminder_path, sep='\t')

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""2015 - 2019 Choropleth Maps of Happiness per Country"""""""""""""''
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# data2015_wh - choropleth
d_data2015_wh = dict(type='choropleth'
                     , locations=data2015_wh['Country']
                     , locationmode='country names'
                     , z=data2015_wh['Happiness Score']
                     , text=data2015_wh['Country']
                     , colorbar={'title': 'Happiness'})
l_data2015_wh = dict(title='Happiness Index 2015'
                     , geo=dict(showframe=False
                                , projection={'type': 'mercator'}))
choropleth2015_wh = go.Figure(data=[d_data2015_wh]
                              , layout=l_data2015_wh)
choropleth2015_wh.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
plot(choropleth2015_wh, filename='choropleth2015.html', auto_open=False)

# data2016_wh - choropleth
d_data2016_wh = dict(type='choropleth'
                     , locations=data2016_wh['Country']
                     , locationmode='country names'
                     , z=data2016_wh['Happiness Score']
                     , text=data2016_wh['Country']
                     , colorbar={'title': 'Happiness'})
l_data2016_wh = dict(title='Happiness Index 2016'
                     , geo=dict(showframe=False
                                , projection={'type': 'mercator'}))
choropleth2016_wh = go.Figure(data=[d_data2016_wh]
                              , layout=l_data2016_wh)
choropleth2016_wh.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
plot(choropleth2016_wh, filename='choropleth2016.html', auto_open=False)

# data2017_wh - choropleth
d_data2017_wh = dict(type='choropleth'
                     , locations=data2017_wh['Country']
                     , locationmode='country names'
                     , z=data2017_wh['Happiness.Score']
                     , text=data2017_wh['Country']
                     , colorbar={'title': 'Happiness'})
l_data2017_wh = dict(title='Happiness Index 2017'
                     , geo=dict(showframe=False
                                , projection={'type': 'mercator'}))
choropleth2017_wh = go.Figure(data=[d_data2017_wh]
                              , layout=l_data2017_wh)
choropleth2017_wh.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
plot(choropleth2017_wh, filename='choropleth2017.html', auto_open=False)

# data2018_wh - choropleth
d_data2018_wh = dict(type='choropleth'
                     , locations=data2018_wh['Country']
                     , locationmode='country names'
                     , z=data2018_wh['Score']
                     , text=data2018_wh['Country']
                     , colorbar={'title': 'Happiness'})
l_data2018_wh = dict(title='Happiness Index 2018'
                     , geo=dict(showframe=False
                                , projection={'type': 'mercator'}))
choropleth2018_wh = go.Figure(data=[d_data2018_wh]
                              , layout=l_data2018_wh)
choropleth2018_wh.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
plot(choropleth2018_wh, filename='choropleth2018.html', auto_open=False)

# data2019_wh - choropleth
d_data2019_wh = dict(type='choropleth'
                     , locations=data2019_wh['Country']
                     , locationmode='country names'
                     , z=data2019_wh['Score']
                     , text=data2019_wh['Country']
                     , colorbar={'title': 'Happiness'})
l_data2019_wh = dict(title='Happiness Index 2019'
                     , geo=dict(showframe=False
                                , projection={'type': 'mercator'}))
choropleth2019_wh = go.Figure(data=[d_data2019_wh]
                              , layout=l_data2019_wh)
choropleth2019_wh.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
plot(choropleth2019_wh, filename='choropleth2019.html', auto_open=False)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""Relationship Between GDP, Life Expectancy, and Perceptions of Corruption"""''
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
x_data = data2019_wh['GDP per capita']
y_data = data2019_wh['Healthy life expectancy'] * 100
z_data = data2019_wh['Perceptions of corruption']

gdp_lifeexpectancy_corruption = go.Figure(data=[go.Scatter3d(
    x=x_data
    , y=y_data
    , z=z_data
    , mode='markers'
    , marker=dict(
        size=6
        , color=z_data
        , colorscale='Viridis'
        , opacity=0.8
    )
)])
