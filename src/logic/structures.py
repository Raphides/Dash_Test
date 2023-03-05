import pandas as pd

class Coin:
  def __init__(self, name: str, acronym: str):
    self.name = name
    self.acronym = acronym
    self.set_minimum_wage(pd.read_excel("./src/logic/tables/Tratado.xlsx"))
    self.start_year = list(self.minimum_wages.index.values)[0][-2:]
    self.final_year = list(self.minimum_wages.index.values)[-1][-2:]

    if int(self.start_year) > 30:
      self.start_year = "19" + self.start_year
    else:
      self.start_year = "20" + self.start_year
    if int(self.final_year) > 30:
      self.final_year = "19" + self.final_year
    else:
      self.final_year = "20" + self.final_year

  def set_minimum_wage(self, data_source: pd.DataFrame):
    data_source = data_source.set_index("LEGISLAÇÃO")
    self.minimum_wages = data_source.loc[lambda df: df[ "MOEDA"] == self.acronym,:]