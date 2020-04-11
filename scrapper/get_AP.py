import os
import pandas as pd
import json
import math
import re

from pandas import ExcelWriter
from pandas import ExcelFile
from unidecode import unidecode

file_path = os.path.join(os.getcwd(), "scrapper",
                         "files", "in", "bairro_ap_novo.xlsx")
write_path = os.path.join(os.getcwd(), "scrapper", "files", "out", "ap.json")
df = pd.read_excel(file_path, "APs - granular")


def remove_end_numbers(xs):
    return re.sub(r'(.*?)\s*\d+', r'\1', xs).strip()


print(df)

df['Bairros'] = df['Unnamed: 1'][2:]
df['AP'] = df['Unnamed: 2'][2:]

for i in range(6):
    df.drop(f'Unnamed: {i}', axis=1, inplace=True)

df.drop(df.index[0], inplace=True)
df.drop(df.index[0], inplace=True)

data = {unidecode(df['Bairros'][i].lower().strip()): df['AP'][i]
        for i in range(2, len(df['AP']))}
print(data)

with open(write_path, 'w') as f:
    json.dump(data, f)
