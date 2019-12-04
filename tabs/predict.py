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

    html.Div(id='prediction-content', style={'fontWeight': 'bold'}),

    html.Div([
        dcc.Markdown('###### Area'),
        dcc.Dropdown(
            id='area',
            options=[{'label': city, 'value': city} for city in cities],
            value=cities[10]
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
            max=15,
            step=1,
            value=3,
            marks={n: str(n) for n in range(2, 15, 1)}
        ),
    ], style=style),

    html.Div([
        dcc.Markdown('###### Listing Price'),
        dcc.Slider(
            id='list_price',
            min=1000000,
            max=3000000,
            step=100000,
            value=1500000,
            marks={n: f'{n/1000:.0f}k' for n in range(1000000, 3000000, 100000)}
        ),
    ], style=style),

])


@app.callback(
    Output('prediction-content', 'children'),
    [Input('area', 'value'),
     Input('bedrooms', 'value'),
     Input('baths', 'value'),
     Input('offers', 'value'),
     Input('list_price', 'value')])
def predict(area, bedrooms, baths, offers, list_price):

    year = 2019
    df = pd.DataFrame(
        columns=['Year', 'Area', 'Total Bathrooms', 'Bedrooms', 'Curr List Price', 'Number of Offers'],
        data=[[year, area, baths, bedrooms, list_price, offers]]
    )

    pipeline = load('model/pipeline.joblib')
    y_pred_log = pipeline.predict(df)
    y_pred = y_pred_log[0]
    percent_over = ((y_pred - list_price) / list_price) * 100
    per_offer = percent_over / offers
    results = f'The predicted winning bid is ${y_pred:,.0f} which is {percent_over:.2f}% over the asking price or \
                {per_offer:.2f}% per offer.'

    return results
