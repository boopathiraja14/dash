import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash
import pandas as pd
from plotly import graph_objects as go
import flask
import google.cloud.logging
import logging

# Instantiates a client
# client = google.cloud.logging.Client()
# client.setup_logging()
#
# logging.getLogger().setLevel(logging.INFO)


# server = flask.Flask(__name__)
# app = flask.Flask(__name__)
# app = dash.Dash(__name__, server)
app = dash.Dash(__name__)
server = app.server

df = pd.read_csv('gapminderDataFiveYear.csv')
year_options = []
for year in df.year.unique():
    year_options.append({'label':str(year), 'value':year})

app.layout = html.Div([
    html.Div('text is only'),
    html.P('some nice graph'),
   dcc.Graph(id='graph'),
   dcc.Dropdown(id='year_picker', options=year_options, value=df['year'].max())
], style=dict(width='48%'))

# @app.route("/", methods=['GET'])
# def home():
    # logging.info('bas shape')
    # return 'good work bas'
#
# app.route('/get_dash')
@app.callback(Output(component_id='graph', component_property='figure'),
              [Input(component_id='year_picker', component_property='value')])
def render_page(input):

    df_year = df[df.year == input]
    traces = []

    fig = go.Figure()
    for cont in df_year['continent'].unique():
        df_cont = df_year[df_year.continent == cont]
        fig.add_trace(go.Scatter(x=df_cont['gdpPercap'], y=df_cont['lifeExp'],
                      mode='markers',
                      opacity=0.7,
                      marker=dict(size=15),
                      name=cont
                      ))

    return fig

# app.run_server()
if __name__ == '__main__':
    # app.run()
    app.run_server()