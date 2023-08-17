from dash import Dash, dash_table, html,dcc
import pandas as pd
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__)

# app layout
app.layout = html.Div([
    html.H1(children="My first app with Dash"),
    dash_table.DataTable(data=df.to_dict("records"), page_size=10),
    dcc.Graph(figure=px.histogram(data_frame=df,x='continent',y='lifeExp', histfunc='avg'))
     
     ]
)

if __name__ == '__main__':
    app.run(debug=True)
