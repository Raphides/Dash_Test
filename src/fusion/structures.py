from logic import Moeda
from dash import html, dcc, Dash

moedas = {
  "Cruzeiro" : Moeda("Cruzeiro", "Cr$"),
  "Cruzeiro Novo" : Moeda("Novo Cruzeiro", "NCr$"),
  "Cruzado" : Moeda("Cruzado", "Cz$"),
  "Cruzado Novo" : Moeda("Novo Cruzado", "NCz$"),
  "Cruzeiro Real" : Moeda("Cruzeiro Real", "CR$"),
  "Real" : Moeda("Real", "R$"),
}

app_layout = html.Div(
    children=[
        html.H1(children="Evolução das Moedas", id="opa"),
    ]
    )