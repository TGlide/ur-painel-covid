import os
import pandas as pd
import json
import math
import re

from pandas import ExcelWriter
from pandas import ExcelFile
from unidecode import unidecode

file_path = os.path.join(os.getcwd(), "scrapper", "bairro_ap_v2.xlsx")
write_path = os.path.join(os.getcwd(), "scrapper", "ap.json")
df = pd.read_excel(file_path)


def remove_end_numbers(xs):
    return re.sub(r'(.*?)\s*\d+', r'\1', xs).strip()


df['Bairros'] = df['Unnamed: 0'].apply(
    remove_end_numbers).apply(lambda x: unidecode(x))[1:]
df['AP'] = df['Unnamed: 1'][1:]

data = {df['Bairros'][i].lower(): df['AP'][i] for i in range(1, len(df['AP']))}

with open(write_path, 'w') as f:
    json.dump(data, f)
