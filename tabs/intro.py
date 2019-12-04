from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
### Intro
Marin County California is one of the most expensive residential real estate markets in the country.  It is also
one of the most competitive markets with more than 45% of all single-family homes in 2018
receiving multiple offers.  How does a buyer or buyer's agent determine the optimal price to bid on a home -
a price high enough to win the bidding war, yet not too high over the next highest bid.  Essentially it is
a classic auction problem.

This web app enables the user to determine the predicted price to pay for a home facing a bidding a war.
The predicted price is based on historical data from 2015 - 2019 for all single-family homes sold in Marin
receiving two or more offers.  The user can select the area, number of bedrooms, number of baths, number of
expected offers and listing price and the app will provide the predicted sales price.

As a rule of thumb, real estate agents have used anywhere from 2 to 3 percent per offer to determine the
price to pay in a bidding war.  For example, if there are 3 offers the bid should be anywhere from 6% to
9% over the list price.
""")]
