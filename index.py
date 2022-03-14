from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app, server
from tabs import intro, predict, explain, evaluate

style = {'maxWidth': '960px', 'margin': 'auto'}

app.layout = html.Div([
    dcc.Markdown('Do you mind Vladimir Putin to become Russian president again?'),
    html.Div(id='tabs-content'),
    dcc.RadioItems(
        options=[
       {'label': 'YES', 'value': 'YES. I don not mind'},
       {'label': 'NO', 'value': 'NO. I don not mind.'},
        ]
       value='YES'
)
], style=style)



if __name__ == '__main__':
    app.run_server(debug=True)
