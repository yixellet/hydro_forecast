from dash import Dash, dcc, html, Input, Output
import json
from getDataFromCSV import dfFromCsv
from dailyPlot import plot

year = 1979

df = dfFromCsv('data/heps/{}.csv'.format(str(year)))

fig = plot(df, 'date', 'common', {'date': 'Дата', 'common': 'Расход'}, title=year)

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
