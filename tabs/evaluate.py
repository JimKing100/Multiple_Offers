from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
### Final Results

The predictions were equal to or greater than the actual winning offer 53.48% of the time.
Several metrics were calculated in order to evaluate the predictions versus the actuals:

|  Metric      |  Result   |
|--------------|-----------|
| Median Error |  0.49%    |
| Within 1%    | 14.69%    |
| Within 5 %   | 69.72%    |
| Within 10%   | 91.49%    |


"""),

html.Img(src='https://raw.githubusercontent.com/JimKing100/Multiple_Offers/master/data/prediction_errors.png')]
