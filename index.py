from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app, server
from tabs import intro, predict, explain, evaluate

style = {'maxWidth': '960px', 'margin': 'auto'}

app.layout = html.Div([
    dcc.Markdown('# Multiple Offer Calculator'),
    dcc.Tabs(id='tabs', value='tab-intro', children=[
        dcc.Tab(label='Intro', value='tab-intro'),
        dcc.Tab(label='Predict', value='tab-predict'),
        dcc.Tab(label='Explain', value='tab-explain'),
        dcc.Tab(label='Evaluate', value='tab-evaluate'),
    ]),
    html.Div(id='tabs-content'),
], style=style)

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-intro': return intro.layout
    elif tab == 'tab-predict': return predict.layout
    elif tab == 'tab-explain': return explain.layout
    elif tab == 'tab-evaluate': return evaluate.layout

if __name__ == '__main__':
    app.run_server(debug=True)
