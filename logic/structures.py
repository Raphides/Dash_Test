import pandas as pd

class Moeda:
  def __init__(self, nome: str, sigla: str):
    self.nome = nome
    self.sigla = sigla
    self.definir_salarios_minimos(pd.read_excel("./tables/Tratado.xlsx"))
    self.ano_inicial = list(self.salarios_minimos.index.values)[0][-2:]
    self.ano_final = list(self.salarios_minimos.index.values)[-1][-2:]

    if int(self.ano_inicial) > 30:
      self.ano_inicial = "19" + self.ano_inicial
    else:
      self.ano_inicial = "20" + self.ano_inicial
    if int(self.ano_final) > 30:
      self.ano_final = "19" + self.ano_final
    else:
      self.ano_final = "20" + self.ano_final

  def definir_salarios_minimos(self, fonte_de_dados: pd.DataFrame):
    fonte_de_dados = fonte_de_dados.set_index("LEGISLAÇÃO")
    self.salarios_minimos = fonte_de_dados.loc[lambda df: df[ "MOEDA"] == self.sigla,:]

