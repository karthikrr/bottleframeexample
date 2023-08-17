from dash import Dash, dash_table, html,dcc, Input,Output,callback
import pandas as pd
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__)

# app layout
app.layout = html.Div([
    html.H1(children="My first app with Dash control and graph"),
    html.Hr(),    
    dash_table.DataTable(data=df.to_dict("records"), page_size=10),
    dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='controls-and-radio-item'),
    dcc.Graph(figure={}, id='controls-and-graph')
     
    ]
)

# adding controls for interaction
@callback(Output(component_id='controls-and-graph', component_property='figure'),
Input(component_id='controls-and-radio-item', component_property='value'))
def update_graph(chosen_option):
    fig = px.histogram(data_frame=df, x='continent', y=chosen_option, histfunc='avg')
    return fig


if __name__ == '__main__':
    app.run(debug=True)
