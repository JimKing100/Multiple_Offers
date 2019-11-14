from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
### Intro
This web app enables you to get a quick, anonymous estimate of what interest rate you could get on
a Lending Club peer-to-peer loan.
Lending Club will give you an estimate directly, but you have to provide your name, and they pull your
credit score. (They say that this does not impact your credit score.)
For an anonymous convenient estimate, I reverse-engineered the Lending Club formula using their public
data and an xgboost model.
This also enables you to do interactive "what-if" analysis!
"""),

html.Img(src='/assets/fabian-blank-pElSkGRA2NU-unsplash.jpg', style={'width':'100%'})]
