# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import os

DEBUG = int(os.environ.get('DEBUG', default=0))
RELOAD = int(os.environ.get('RELOAD', default=1))

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='Ultimate Containers, by Hiram Foster'),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1], 'y': [4], 'type': 'bar', 'name': 'SF'},
                {'x': [1], 'y': [2], 'type': 'bar', 'name': u'NY'},
            ],
            'layout': {'title': 'Dash Data Visualization'}
        }
    )
])

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", debug=DEBUG, use_reloader=RELOAD)