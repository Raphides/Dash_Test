from logic import Coin
from dash import html, dcc, Dash

moedas = {
  "Cruzeiro" : Coin("Cruzeiro", "Cr$"),
  "Cruzeiro Novo" : Coin("Novo Cruzeiro", "NCr$"),
  "Cruzado" : Coin("Cruzado", "Cz$"),
  "Cruzado Novo" : Coin("Novo Cruzado", "NCz$"),
  "Cruzeiro Real" : Coin("Cruzeiro Real", "CR$"),
  "Real" : Coin("Real", "R$"),
}

chooser = dcc.RadioItems(
    options=["Inicio"] + list(moedas.keys()),
    value="Início",
    className="Opções"
)

app_layout = html.Div(
    children=[
        html.H1(children="Evolução das Moedas", id="opa"),
        chooser
    ]
    )