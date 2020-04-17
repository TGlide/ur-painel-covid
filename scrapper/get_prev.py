import os
import pandas as pd
import json
from pandas import ExcelWriter
from pandas import ExcelFile
import math
from pprint import pprint as pp


def date_to_str(dt):
    months = [
        "Jan",
        "Feb",
        "Mar",
        "Abr",
        "Mai",
        "Jun",
        "Jul",
        "Ago",
        "Set",
        "Out",
        "Nov",
        "Dez"
    ]
    month = months[int(dt[5:7]) - 1]
    day = dt[8:10]
    return f"{month} {day}"


file_path = os.path.join(os.getcwd(), "scrapper",
                         "files", "in", "previsao_casos.csv")
write_path = os.path.join(os.getcwd(), "scrapper", "files", "out", "prev.json")
write_csv_path = os.path.join(
    os.getcwd(), "scrapper", "files", "out", "prev.csv")


df = pd.read_csv(file_path, delimiter=";")

df['date'] = df['date'].apply(date_to_str)

res = []
previous_cases = {}
diario = []
dfT = df.T
for i in range(336, -1, -1):
    entry = dict(dfT[i])
    entry['diario'] = entry['casos'] - previous_cases[entry['city']]  \
        if entry['city'] in previous_cases else entry['casos']
    previous_cases[entry['city']] = entry['casos']
    res.append(entry)
    diario.append(entry['diario'])

df['diario'] = list(reversed(diario))
df.to_csv(write_csv_path, index=False)

data = {
    "city": {
        "labels": [],
        "total": [],
        "daily": []
    },
    "state": {
        "labels": [],
        "total": [],
        "daily": []
    }
}

for i in range(len(df) - 1, -1, -1):
    date, city, casos, diario = df['date'][i], df['city'][i], df['casos'][i], df['diario'][i]
    if city not in ["Rio de Janeiro", "Estado RJ"]:
        continue

    city = "city" if city == 'Rio de Janeiro' else "state"

    data[city]["labels"].append(date)
    data[city]["total"].append(int(casos))
    data[city]["daily"].append(int(diario))

print(data['state']['labels'].index('Abr 16'))
print(data['state']['daily'][34:])
print(data['state']['total'][34:])
print(data['state']['labels'][34:])
print()
print(data['city']['labels'].index('Abr 16'))
print(data['city']['daily'][33:])
print(data['city']['total'][33:])
print(data['city']['labels'][33:])

with open(write_path, 'w') as f:
    json.dump(data, f)
