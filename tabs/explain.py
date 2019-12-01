from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
#### The Project Goal and Data

The goal of the project is to predict the optimal offer for a single-family home in Marin county California
in a multiple offer situation - a bidding war.  The key factors in determining the optimal offer include
the area (city), the listing price, the number of bedrooms, the number of baths and the number of total expected
offers.

#### The Data and Evaluation Protocol
Since I have a real estate license I have access to the Marin MLS which I used to download 5 years (2015 – 2019)
of single-family home sales with more than one offer.  The data was divided into training (2015 - 2017) with 2,973 sales,
validation (2018) with 991 sales and test (2019) with 776 sales.  The test set contains about 11 months of data from 2019.

#### Model Selection
A simple linear regression was initially run with excellent results.  An XGBoost model was then run and had
slightly better metrics and was therefore selected as the model.

|           | Validation | Test     |
|-----------|------------|----------|
| MAE       | $71,851    | $68,002  |
| R-Squared | 0.9726     | 0.9839   |


""")]
