"""
https://www.youtube.com/watch?v=vqVwpL4bGKY&list=PLh3I780jNsiS3xlk-eLU2dpW3U-wCq4LW



"""

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

from pathlib import Path

filename = "~/projects/Dash-by-Plotly/Dataset/Berlin_crimes.csv.gz"
data_path = Path(filename)
df = pd.read_csv(data_path, compression='gzip')

df = pd.read_csv("Berlin_crimes.csv.gz", compression='gzip')

df = df.groupby('District')[['Street_robbery', 'Drugs']].median()

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div([
        dbc.Row(dbc.Col(html.H3("Our Beautiful App Layout"),
                        width={'size': 6, 'offset': 3},
                        ),
                ),
        dbc.Row(dbc.Col(html.Div("One column is all we need because there ain't no room for the "
                                 "both of us in this raggedy town"),
                        width=12
                        )
                ),
        dbc.Row(
            [
                dbc.Col(dcc.Dropdown(id='a_dropdown', placeholder='first dropdown',
                                     options=[{'label': 'Option A', 'value': 'optA'},
                                              {'label': 'Option B', 'value': 'optB'}]),
                        width={'size': 4, "offset": 1, 'order': 1}
                        ),
                dbc.Col(dcc.Dropdown(id='b_dropdown', placeholder='middle dropdown',
                                     options=[{'label': 'Option A', 'value': 'optA'},
                                              {'label': 'Option B', 'value': 'optB'}]),
                        width={'size': 2,  "offset": 0, 'order': 2}
                        ),
                dbc.Col(dcc.Dropdown(id='c_dropdown', placeholder='last dropdown',
                                     options=[{'label': 'Option A', 'value': 'optA'},
                                              {'label': 'Option B', 'value': 'optB'}]),
                        width={'size': 3, "offset": 1, 'order': 3}
                        ),
            ], no_gutters=True
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='pie_chart1', figure={}),
                        width=5, lg={'size': 6,  "offset": 0, 'order': 'first'}
                        ),
                dbc.Col(dcc.Graph(id='pie_chart2', figure={}),
                        width=5, lg={'size': 6,  "offset": 0, 'order': 'last'}
                        ),
            ]
        )
])


@app.callback(
    [Output('pie_chart1', 'figure'),
     Output('pie_chart2', 'figure')],
    [Input('a_dropdown', 'value'),
     Input('b_dropdown', 'value'),
     Input('c_dropdown', 'value')]
)
def update_graph(dpdn_a, dpdn_b, dpdn_c):
    dff = df[:200]
    if dpdn_a is None or dpdn_b is None or dpdn_c is None:
        pie_fig = px.pie(dff, names=dff.index, values='Street_robbery', title='Street Robbery')\
            .update_layout(showlegend=False, title_x=0.5)\
            .update_traces(textposition='inside',  textinfo='label+percent')
        pie_fig2 = px.pie(dff, names=dff.index, values='Drugs', title='Drugs')\
            .update_layout(showlegend=False, title_x=0.5)\
            .update_traces(textposition='inside', textinfo='label+percent')
        return pie_fig, pie_fig2
    else:
        raise dash.exceptions.PreventUpdate


if __name__ == "__main__":
    app.run_server(debug=True, port=8080)
