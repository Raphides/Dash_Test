import pandas as pd
from dash import Dash
from logic import *
from visuals import *
from fusion import *

app = Dash(__name__)

app.layout = app_layout

if __name__ == "__main__":
    app.run_server(debug=True)