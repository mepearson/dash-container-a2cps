import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly
import plotly.express as px
import pathlib
import os

################################################################################
##                                                                            ##
##  Devops                                                                    ##
##                                                                            ##
################################################################################

DATA_PATH = pathlib.Path(__file__).parent.joinpath("data") 
ASSETS_PATH = pathlib.Path(__file__).parent.joinpath("assets")
REQUESTS_PATHNAME_PREFIX = os.environ.get("REQUESTS_PATHNAME_PREFIX", "/")

app = dash.Dash(
    __name__,
    assets_folder=ASSETS_PATH,
    requests_pathname_prefix=REQUESTS_PATHNAME_PREFIX,
)

app.layout = html.Div("A plotly-dash container")

if __name__ == '__main__':
    app.run_server(debug=True)
else:
    server = app.server
