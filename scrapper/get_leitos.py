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
          'Total Leitos SUS (excluindo neonatal)', 'Bairro (cidade Rio de Janeiro)']]

data = {
    "estado": {},
    "municipio": {}
}
for index, row in df1.iterrows():

    if type(row['Bairro (cidade Rio de Janeiro)']) == float:
        if row['Cidade'] not in data['estado']:
            data['estado'][row['Cidade']] = {'Total': row['Total Leitos (excluindo neonatal)'],
                                             "SUS": row['Total Leitos SUS (excluindo neonatal)']}
        else:
            data['estado'][row['Cidade']
                           ]['Total'] += row['Total Leitos (excluindo neonatal)']
            data['estado'][row['Cidade']
                           ]['SUS'] += row['Total Leitos SUS (excluindo neonatal)']
    else:
        if row['Bairro (cidade Rio de Janeiro)'] not in data['municipio']:
            data['municipio'][row['Bairro (cidade Rio de Janeiro)']
                              ] = {'Total': row['Total Leitos (excluindo neonatal)'],
                                   "SUS": row['Total Leitos SUS (excluindo neonatal)']}
        else:
            data['municipio'][row['Bairro (cidade Rio de Janeiro)']
                              ]['Total'] += row['Total Leitos (excluindo neonatal)']
            data['municipio'][row['Bairro (cidade Rio de Janeiro)']
                              ]['SUS'] += row['Total Leitos SUS (excluindo neonatal)']

# jsonUau = df2.to_json()
with open(write_path, 'w') as f:
    json.dump(data, f)
