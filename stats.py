from dash import Dash, dcc, html, Input, Output
import json
from config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER, HEPS_TABLE
from connection import connectToDB
from getData import getData
from dailyPlot import plot

(connection, cursor) = connectToDB(
    DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME)

year = 2012

df = getData(cursor, HEPS_TABLE, year=year)

fig = plot(df, 'date', ['common', 'diff'], {'date': 'Дата', 'value': 'Расход'}, title=year)

app = Dash(__name__)

app.layout = html.Div([
    html.H4('Displaying figure structure as JSON'),
    dcc.Graph(id="figure-structure-x-graph", figure=fig),
    dcc.Clipboard(target_id="structure"),
    html.Pre(
        id='figure-structure-x-structure',
        style={
            'border': 'thin lightgrey solid', 
            'overflowY': 'scroll',
            'height': '275px'
        }
    ),
])


@app.callback(
    Output("figure-structure-x-structure", "children"), 
    Input("figure-structure-x-graph", "figure"))
def display_structure(fig_json):
    return json.dumps(fig_json, indent=2)

app.run_server(debug=True)
