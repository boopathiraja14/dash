import plotly.express as px
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd

# app = dash.Dash()
#
# data= pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv")
#
# app.layout = html.Div(dcc.Graph(id='sctter', figure={'data'})
# )
# # fig = px.scatter(x=np.arange(1,101), y=np.random.randint(1,10,100))
# # fig.show()

# if __name__ == '__main__':
#     app.run_server()

fig = go.Figure()
fig.add_trace(go.Scatter(x=[1,2,43], y=[4,5,6]))
fig.show()