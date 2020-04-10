import os
import pandas as pd
import json
from pandas import ExcelWriter
from pandas import ExcelFile
import math

file_path = os.path.join(os.getcwd(), "scrapper", "leitos.xlsx")
write_path = os.path.join(os.getcwd(), "scrapper", "leitos.json")
df = pd.read_excel(file_path)
df1 = df[['UF', 'Cidade', 'Total Leitos (excluindo neonatal)',
          'Total Leitos SUS (excluindo neonatal)', 'Bairro (cidade Rio de Janeiro)', 'Leitos de UTI (excluindo neonatal)', 'Leitos de UTI SUS (excluindo neonatal)']]

data = {
    "estado": {},
    "municipio": {}
}

rows_to_get = {
    "Total":  "Total Leitos (excluindo neonatal)",
    "SUS":  "Total Leitos SUS (excluindo neonatal)",
    "UTI":  "Leitos de UTI (excluindo neonatal)",
    "UTI_SUS":  "Leitos de UTI SUS (excluindo neonatal)",
}

for index, row in df1.iterrows():

    if type(row['Bairro (cidade Rio de Janeiro)']) == float:
        if row['Cidade'] not in data['estado']:
            data['estado'][row['Cidade']] = {key: row[value] for key, value in rows_to_get.items()}
        else:
            for key, value in rows_to_get.items():
                data['estado'][row['Cidade']][key] += row[value]

    else:
        if row['Bairro (cidade Rio de Janeiro)'] not in data['municipio']:
            data['municipio'][row['Bairro (cidade Rio de Janeiro)']] = {key: row[value] for key, value in rows_to_get.items()}
        else:
            for key, value in rows_to_get.items():
                data['municipio'][row['Bairro (cidade Rio de Janeiro)']][key] += row[value]
        

# print(sum([a['Total'] for a in data['estado'].values()]))
# print(sum([a['Total'] for a in data['municipio'].values()]))

susEstado = sum

utiEstado = sum([a['UTI'] for a in data['estado'].values()])
utiCidade = sum([a['UTI'] for a in data['municipio'].values()])

print(
    f"UTIs Estado (Fora do Municipio): {utiEstado } | 60% -> {int(utiEstado *0.6)} | 40% -> {int(utiEstado *0.4)}")
print(
    f"UTIs Estado: {utiEstado + utiCidade} | 60% -> {int((utiEstado + utiCidade)*0.6)} | 40% -> {int((utiEstado + utiCidade) *0.4)}")
print(
    f"UTIs Cidade: { utiCidade} | 60% -> {int(utiCidade*0.6)}\n | 40% -> {int(utiCidade *0.4)}")

utiSusEstado = sum([a['UTI_SUS'] for a in data['estado'].values()])
utiSusCidade = sum([a['UTI_SUS'] for a in data['municipio'].values()])

print(
    f"UTIs SUS Estado (Fora do Municipio): {utiSusEstado} | 60% -> {int(utiSusEstado*0.6)} | 40% -> {int(utiSusEstado *0.4)}")
print(
    f"UTIs SUS Estado: {utiSusEstado + utiSusCidade} | 60% -> {int((utiSusEstado + utiSusCidade )*0.6)} | 40% -> {int((utiSusEstado + utiSusCidade) *0.4)}")
print(
    f"UTIs SUS Cidade: { utiSusCidade} | 60% -> {int(utiSusCidade*0.6)} | 40% -> {int(utiSusCidade *0.4)}")


with open(write_path, 'w') as f:
    json.dump(data, f)
