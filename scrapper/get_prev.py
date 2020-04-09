import os
import pandas as pd
import json
from pandas import ExcelWriter
from pandas import ExcelFile
import math

file_path = os.path.join(os.getcwd(), "scrapper", "prevUERJ.xlsx")
write_path = os.path.join(os.getcwd(), "scrapper", "prevUERJ.json")
df = pd.read_excel(file_path)

data = {
    "otimista": [],
    "esperado": [],
    "pessimista": []

}

fuck = 0
for index, row in df.iterrows():
    fuck += 1
    if fuck >= 9:
        data["otimista"].append(row["Cenário otimista"])
        data["esperado"].append(row["Cenário esperado"])
        data["pessimista"].append(row["Cenário pessimista"])


# jsonUau = df2.to_json()
with open(write_path, 'w') as f:
    json.dump(data, f)
