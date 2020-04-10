import os
import pandas as pd
import json
import math
import re

from pandas import ExcelWriter
from pandas import ExcelFile
from pprint import pprint as pp

FILE_PATH = os.path.join(os.getcwd(), "scrapper", "sequence.csv")

WRITE_PATH = os.path.join(os.getcwd(), "scrapper", "infected_chart.json")


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
    day = dt[-2:]
    return f"{month} {day}"


def getHistoricFromKey(key, df):
    total = [int(i) for i in reversed(df[key])]
    daily = [int(total[0])] + [int(total[i] - total[i-1])
                               for i in range(1, len(total))]
    return {
        "total": total,
        "daily": daily
    }


df = pd.read_csv(FILE_PATH)

data = {
    'confirmed': getHistoricFromKey('confirmed', df),
    'dead': getHistoricFromKey('dead', df),
    'hospitalized': getHistoricFromKey('hospitalized', df),
    'uti': getHistoricFromKey('uti', df),
    'days': [date_to_str(dt) for dt in reversed(df['date'])]
}

with open(WRITE_PATH, 'w') as f:
    json.dump(data, f)
