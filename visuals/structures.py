from dash import html, dcc
from logic.structures import Moeda


class Pagina_do_Dashboard(html.Div):
    def __init__(self, moeda: Moeda):
        self.moeda_referente = moeda
        self.titulo = html.H1(children=self.moeda_referente.nome, className="Título_da_página")
        super().__init__(children=[self.titulo], className="pagina_dash")

class Opção_de_Moeda(html.Li):
    def __init__(self, pagina_associada: Pagina_do_Dashboard):
        self.pagina_associada = pagina_associada
        self.moeda_associada = pagina_associada.moeda_referente
        self.link_da_pagina = html.A(children=self.moeda_associada.nome)
        super().__init__(children=, className="botão_moeda")

class SideBar(html.Ul):
    def __init__(self, children=None):
        super().__init__(children)