# DASH
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
# PLOTLY
import plotly_express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
# OTHER LIBRARIES
import os
import pandas as pd


external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
port = int(os.environ.get("PORT", 5000))
# app.scripts.config.serve_locally=True

##############################################
# DATA
##############################################

df = pd.read_csv("data/gapminder.csv")


##############################################
# HELPER FUNCTION
##############################################

##############################################
# APP LAYOUT
##############################################

app.layout = html.Div(children=[
    html.H1(children="Gapminder Data"),
    html.Div(children="Dash: A web application framework for Python."),
    dcc.Graph(id="plot_01"),
    dcc.Dropdown(
        id="input_01",
        options=[{"label": i, "value": i}
                 for i in list(df["country"].unique())],
        placeholder="Select a country"

    ),
    html.Br()
])

##############################################
# APP CALLBACKS
##############################################


@app.callback(
    dash.dependencies.Output("plot_01", "figure"),
    [dash.dependencies.Input("input_01", "value")]
)
def update_plot_01(selected_country):
    if selected_country == None:
        df_filtered = df
    else:
        df_filtered = df.query("country == @selected_country")
    fig = px.line(
        df_filtered,
        x="year",
        y="pop",
        color="country",
        title="Population"
    )
    return fig


if __name__ == "__main__":
    app.run_server(debug=False,
                   host="0.0.0.0",
                   port=port)
