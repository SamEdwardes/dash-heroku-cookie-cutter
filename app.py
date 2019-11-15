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
import pandas as pd


external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
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
    html.Br(),
    html.Br(),
    dash_table.DataTable(
        id="table_01",
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.head().to_dict("rows")
    )
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

# check it


if __name__ == "__main__":
    app.run_server(debug=True,
                   port=8050)
