import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot

world_happiness_path = "datasets/world-happiness/"
gapminder_path = "datasets/gapminder/datasets_5533_8279_gapminder.tsv"

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
plot(choropleth2015_wh, filename='DataVisualizations/choropleth2015.html', auto_open=False)

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
plot(choropleth2016_wh, filename='DataVisualizations/choropleth2016.html', auto_open=False)

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
plot(choropleth2017_wh, filename='DataVisualizations/choropleth2017.html', auto_open=False)

# data2018_wh - choropleth
d_data2018_wh = dict(type='choropleth'
                     , locations=data2018_wh['Country or region']
                     , locationmode='country names'
                     , z=data2018_wh['Score']
                     , text=data2018_wh['Country or region']
                     , colorbar={'title': 'Happiness'})
l_data2018_wh = dict(title='Happiness Index 2018'
                     , geo=dict(showframe=False
                                , projection={'type': 'mercator'}))
choropleth2018_wh = go.Figure(data=[d_data2018_wh]
                              , layout=l_data2018_wh)
choropleth2018_wh.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
plot(choropleth2018_wh, filename='DataVisualizations/choropleth2018.html', auto_open=False)

# data2019_wh - choropleth
d_data2019_wh = dict(type='choropleth'
                     , locations=data2019_wh['Country or region']
                     , locationmode='country names'
                     , z=data2019_wh['Score']
                     , text=data2019_wh['Country or region']
                     , colorbar={'title': 'Happiness'})
l_data2019_wh = dict(title='Happiness Index 2019'
                     , geo=dict(showframe=False
                                , projection={'type': 'mercator'}))
choropleth2019_wh = go.Figure(data=[d_data2019_wh]
                              , layout=l_data2019_wh)
choropleth2019_wh.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
plot(choropleth2019_wh, filename='DataVisualizations/choropleth2019.html', auto_open=False)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""Relationship Between GDP, Life Expectancy, and Perceptions of Corruption"""''
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
x_data_c = data2019_wh['GDP per capita']
y_data_c = data2019_wh['Healthy life expectancy'] * 100
z_data_c = data2019_wh['Perceptions of corruption']

gdp_life_corruption = go.Figure(data=[go.Scatter3d(
    x=x_data_c
    , y=y_data_c
    , z=z_data_c
    , mode='markers'
    , text=data2019_wh['Country or region']
    , marker=dict(
        size=6
        , color=z_data_c
        , colorscale='Viridis'
        , opacity=0.8
    )
)])

gdp_life_corruption.update_layout(scene=dict(
            xaxis_title="GDP Per Capita ($100,000s)"
            , yaxis_title="Healthy Life Expectancy (Years)"
            , zaxis_title="Perceptions of Corruption"
        )
    , title="GDP vs Life Expectancy vs Corruption"
    , margin=dict(l=0, r=0, b=0, t=0)
)

plot(gdp_life_corruption, filename ='DataVisualizations/gdp_lifeExp_corruption.html', auto_open=False)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""Relationship Between GDP, Life Expectancy, and Freedom'"""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
x_data_f = data2019_wh['Freedom to make life choices']
y_data_f = data2019_wh['Healthy life expectancy'] * 100
z_data_f = data2019_wh['GDP per capita']

gdp_life_freedom = go.Figure(data=[go.Scatter3d(
    x=x_data_f
    , y=y_data_f
    , z=z_data_f
    , mode='markers'
    , text=data2019_wh['Country or region']
    , marker=dict(
        size=6
        , color=z_data_f
        , colorscale='Viridis'
        , opacity=0.8
    )
)])

gdp_life_freedom.update_layout(scene=dict(
            xaxis_title="Freedom to Make Life Choices"
            , yaxis_title="Healthy Life Expectancy (Years)"
            , zaxis_title="GDP Per Capita ($100,000s)"
        )
    , title="GDP vs Life Expectancy vs Corruption"
    , margin=dict(l=0, r=0, b=0, t=0)
)

plot(gdp_life_freedom, filename ='DataVisualizations/gdp_lifeExp_freedom.html', auto_open=False)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""Relationship Between GDP and Life Expectancy"""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
gapminder_data = px.data.gapminder()
gdp_lifeExp = px.scatter(
    gapminder_data
    , x="gdpPercap"
    , y="lifeExp"
    , animation_frame="year"
    , animation_group="country"
    , size="pop"
    , color="continent"
    , hover_name="country"
    , log_x=True
    , size_max=55
    , range_x=[100, 100000]
    , range_y=[25, 90]
)

gdp_lifeExp.update_layout(
    xaxis_title="GDP Per Capita ($)"
    , yaxis_title="Life Expectancy (Years)"
    , title="GDP VS Life Expectancy"
    , margin=dict(l=0, r=0, b=0, t=40)
)

plot(gdp_lifeExp, filename='DataVisualizations/gdp_lifeExp.html', auto_open=False)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""Relationship Between GDP and Happiness Index"""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
gdp_happiness = go.Figure(data=go.Scatter(
    x=data2019_wh['GDP per capita']
    , y=data2019_wh['Score']
    , mode='markers'
    , hovertext=data2019_wh['Country or region']
    , marker=dict(
        size=data2019_wh['Score'] ** 1.8
        , color=data2019_wh['Score']
    )
))

gdp_happiness.update_layout(
    xaxis_title='GDP Per Capita ($100,000s)'
    , yaxis_title='Happiness Score'
    , title="GDP Vs Happiness"
    , margin=dict(l=0, r=0, b=0, t=40)
)

plot(gdp_happiness, filename='DataVisualizations/gdp_happiness.html', auto_open=False)
