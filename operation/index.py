import pandas as pd
from dash import html, dcc, Dash
from logic.structures import Moeda

moedas = {
  "Cruzeiro" : Moeda("Cruzeiro", "Cr$"),
  "Cruzeiro Novo" : Moeda("Novo Cruzeiro", "NCr$"),
  "Cruzado" : Moeda("Cruzado", "Cz$"),
  "Cruzado Novo" : Moeda("Novo Cruzado", "NCz$"),
  "Cruzeiro Real" : Moeda("Cruzeiro Real", "CR$"),
  "Real" : Moeda("Real", "R$"),
}

my_css = [
    {
    "href": "./assets/style.css",
    "rel": "stylesheets",
    "type": "text/css",
    }
]

app = Dash(__name__, external_stylesheets=my_css)

app.layout = html.Div(
    children=[
        html.H1(children="Evolução das Moedas"),
        
    ]
    )

if __name__ == "__main__":
    app.run_server(debug=True)