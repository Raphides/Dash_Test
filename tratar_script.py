import pandas as pd
import numpy as np

main_table = pd.read_excel("evolucao_do_salario_minimo.xls")
main_table = main_table.drop(range(3), axis=0)
main_table.iloc[0,3] = "MOEDA"
main_table.iloc[0,5] = "Delete1"
main_table.iloc[0,6] = "Delete2"
main_table.columns = main_table.iloc[0]
main_table = main_table.drop(range(3, 6))
main_table = main_table.drop(["Delete1", "Delete2"], axis = 1)
to_delete = list(range(51,58))
to_delete.extend(list(range(102, 110)))
to_delete.extend(list(range(150, 162)))
main_table = main_table.drop(to_delete, axis=0)
for category in ["LEGISLAÇÃO", "MOEDA"]:
  main_table[category] = main_table[category].str.strip()

main_table = main_table.set_index("LEGISLAÇÃO")
main_table.to_excel("Tratado.xlsx")
main_table.to_csv("Tratado.csv")
