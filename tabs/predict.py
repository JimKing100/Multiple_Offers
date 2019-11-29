from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from joblib import load
import numpy as np
import pandas as pd

from app import app

cities = ['Belvedere',
          'Bolinas',
          'Corte Madera',
          'Dillon Beach',
          'Fairfax',
          'Greenbrae',
          'Inverness',
          'Kentfield',
          'Larkspur',
          'Marshall',
          'Mill Valley',
          'Muir Beach',
          'Nicasio',
          'Novato',
          'Point Reyes',
          'Ross',
          'San Anselmo',
          'San Geronimo Valley',
          'San Rafael',
          'Sausalito',
          'Stinson Beach',
          'Tiburon',
          'Tomales',
          'Other'
          ]

style = {'padding': '1.5em'}

layout = html.Div([
    dcc.Markdown("""
        ### Predict
        Use the controls below to update your predicted offer, based on city,
        beds, baths, number of offers, and list price.

    """),

    html.Div(id='prediction-content', style={'fontWeight':'bold'}),

    html.Div([
        dcc.Markdown('###### Area'),
        dcc.Dropdown(
            id='area',
            options=[{'label': city, 'value': city} for city in cities],
            value=cities[0]
        ),
    ], style=style),

    html.Div([
        dcc.Markdown('###### Bedrooms'),
        dcc.Slider(
            id='bedrooms',
            min=1,
            max=7,
            step=1,
            value=3,
            marks={n: str(n) for n in range(1, 7, 1)}
        ),
    ], style=style),

    html.Div([
        dcc.Markdown('###### Baths'),
        dcc.Slider(
            id='baths',
            min=1,
            max=9,
            step=1,
            value=2,
            marks={n: str(n) for n in range(1, 9, 1)}
        ),
    ], style=style),

    html.Div([
        dcc.Markdown('###### Number of Offers'),
        dcc.Slider(
            id='offers',
            min=2,
            max=28,
            step=1,
            value=2,
            marks={n: str(n) for n in range(2, 28, 1)}
        ),
    ], style=style),

    html.Div([
        dcc.Markdown('###### Listing Price'),
        dcc.Slider(
            id='list_price',
            min=250000,
            max=5000000,
            step=25000,
            value=1000000,
            marks={n: f'{n/1000:.0f}k' for n in range(250000, 5000000, 25000)}
        ),
    ], style=style),

])

@app.callback(
    Output('prediction-content', 'children'),
    [Input('cities', 'value'),
     Input('bedrooms', 'value'),
     Input('baths', 'value'),
     Input('offers', 'value'),
     Input('list_price', 'value')])
def predict(cities, bedrooms, baths, offers, list_price):

    year = 2019
    df = pd.DataFrame(
        columns=['Year', 'Area', 'Total Bathrooms', 'Bedrooms', 'Curr List Price', 'Number of Offers'],
        data=[[year, area, baths, bedrooms, list_price, offers]]
    )

    pipeline = load('model/pipeline.joblib')
    y_pred_log = pipeline.predict(df)
    y_pred = np.expm1(y_pred_log)[0]

    return y_pred
