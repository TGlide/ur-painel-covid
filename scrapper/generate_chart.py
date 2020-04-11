import os
import re
import math
import json
import pandas as pd

from pandas import ExcelWriter
from pandas import ExcelFile
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


def getHistoricFromList(xl, reverse=True):
    total = [int(i) for i in xl]
    if reverse:
        total = list(reversed(total))
    daily = [int(total[0])] + [int(total[i] - total[i-1])
                               for i in range(1, len(total))]
    return {
        "total": total,
        "daily": daily
    }


def getHistoricFromKey(key, df, reverse=True):
    return getHistoricFromList(df[key], reverse=reverse)


def getUpperBound(num):
    n_digits = math.floor(math.log10(num))
    return math.ceil(num/10**n_digits)*(10**n_digits)


CHART_TEMPLATE = os.path.join(
    os.getcwd(), "scrapper", "files", "in", "chart_template.json")
HISTORIC_DATA = os.path.join(
    os.getcwd(), "scrapper", "files", "in", "sequence.csv")
PROJECTION_DATA = os.path.join(
    os.getcwd(), "scrapper", "files", "in", "prevUERJ.xlsx")
PROJECTION_SP_DATA = os.path.join(
    os.getcwd(), "scrapper", "files", "in", "prevBaseSP.xlsx")
WRITE_PATH = os.path.join(
    os.getcwd(), "src", "data",  "charts.json")


f = open(CHART_TEMPLATE, 'r')
template = json.load(f)
f.close()

historicDF = pd.read_csv(HISTORIC_DATA)

data = {
    'confirmed': getHistoricFromKey('confirmed', historicDF),
    'fatal': getHistoricFromKey('dead', historicDF),
    'hospitalized': getHistoricFromKey('hospitalized', historicDF),
    'uti': getHistoricFromKey('uti', historicDF),
    'days': [date_to_str(dt) for dt in reversed(historicDF['date'])]
}

template['confirmed']['data']['labels'] = data['days']
template['confirmed']['data']['datasets']['Município'][0]['data'] = data['confirmed']['daily']
template['confirmed']['data']['datasets']['Município'][1]['data'] = data['confirmed']['total']

template['hospitalized']['data']['labels'] = data['days']
template['hospitalized']['data']['datasets']['Município'][0]['data'] = data['hospitalized']['daily']
template['hospitalized']['data']['datasets']['Município'][1]['data'] = data['hospitalized']['total']
template['hospitalized']['options']['scales']['yAxes'][0]['ticks']['max'] = getUpperBound(
    max(data['hospitalized']['total']))

template['uti']['data']['labels'] = data['days']
template['uti']['data']['datasets']['Município'][0]['data'] = data['uti']['daily']
template['uti']['data']['datasets']['Município'][1]['data'] = data['uti']['total']
template['uti']['options']['scales']['yAxes'][0]['ticks']['max'] = getUpperBound(
    max(data['uti']['total']))

template['fatal']['data']['labels'] = data['days']
template['fatal']['data']['datasets']['Município'][0]['data'] = data['fatal']['daily']
template['fatal']['data']['datasets']['Município'][1]['data'] = data['fatal']['total']
template['fatal']['options']['scales']['yAxes'][0]['ticks']['max'] = getUpperBound(
    max(data['fatal']['total']))


projectionDF = pd.read_excel(PROJECTION_DATA)

projectionDays = [date_to_str(str(dt)) for dt in projectionDF['Dias']]
starting_point = projectionDays.index(data['days'][-1]) + 1

projData = {
    'otimista': getHistoricFromList(
        list(projectionDF['Cenário otimista'][starting_point:]), reverse=False),
    'esperado': getHistoricFromList(
        list(projectionDF['Cenário esperado'][starting_point:]), reverse=False),
    'pessimista': getHistoricFromList(
        list(projectionDF['Cenário pessimista'][starting_point:]), reverse=False),
}

projData['otimista']['daily'][0] = projData['otimista']['total'][0] - \
    data['confirmed']['total'][-1]

projData['esperado']['daily'][0] = projData['esperado']['total'][0] - \
    data['confirmed']['total'][-1]

projData['pessimista']['daily'][0] = projData['pessimista']['total'][0] - \
    data['confirmed']['total'][-1]

template['confirmed']['projected']['data']['labels'] = projectionDays[starting_point:]

template['confirmed']['projected']['data']['datasets']['UERJ - Otimista'][0]['data'] = projData['otimista']['daily']
template['confirmed']['projected']['data']['datasets']['UERJ - Otimista'][1]['data'] = projData['otimista']['total']

template['confirmed']['projected']['data']['datasets']['UERJ - Esperado'][0]['data'] = projData['esperado']['daily']
template['confirmed']['projected']['data']['datasets']['UERJ - Esperado'][1]['data'] = projData['esperado']['total']

template['confirmed']['projected']['data']['datasets']['UERJ - Pessimista'][0]['data'] = projData['pessimista']['daily']
template['confirmed']['projected']['data']['datasets']['UERJ - Pessimista'][1]['data'] = projData['pessimista']['total']

projectionSpDf = pd.read_excel(PROJECTION_SP_DATA)

print(projectionSpDf)

projectionSPDays = [date_to_str(str(dt)) for dt in projectionSpDf['data']]
starting_point = projectionSPDays.index(data['days'][-1]) + 1
print(projectionSPDays[starting_point:])

projSpData = {
    'otimista': getHistoricFromList(
        list(projectionSpDf['lwr'][starting_point:]), reverse=False),
    'esperado': getHistoricFromList(
        list(projectionSpDf['fit'][starting_point:]), reverse=False),
    'pessimista': getHistoricFromList(
        list(projectionSpDf['upr'][starting_point:]), reverse=False),
}

pp(projSpData)


projSpData['otimista']['daily'][0] = projSpData['otimista']['total'][0] - \
    data['confirmed']['total'][-1]

projSpData['esperado']['daily'][0] = projSpData['esperado']['total'][0] - \
    data['confirmed']['total'][-1]

projSpData['pessimista']['daily'][0] = projSpData['pessimista']['total'][0] - \
    data['confirmed']['total'][-1]

template['confirmed']['projected - est']['data']['labels'] = sorted(list(
    set(projectionSPDays[starting_point:])))

template['confirmed']['projected - est']['data']['datasets']['SP - Otimista'][0]['data'] = projSpData['otimista']['daily']
template['confirmed']['projected - est']['data']['datasets']['SP - Otimista'][1]['data'] = projSpData['otimista']['total']

template['confirmed']['projected - est']['data']['datasets']['SP - Esperado'][0]['data'] = projSpData['esperado']['daily']
template['confirmed']['projected - est']['data']['datasets']['SP - Esperado'][1]['data'] = projSpData['esperado']['total']

template['confirmed']['projected - est']['data']['datasets']['SP - Pessimista'][0]['data'] = projSpData['pessimista']['daily']
template['confirmed']['projected - est']['data']['datasets']['SP - Pessimista'][1]['data'] = projSpData['pessimista']['total']

# template['confirmed']['options']['scales']['yAxes'][0]['ticks']['max'] = getUpperBound(
#     max(projData['pessimista']['total'] + projSpData['pessimista']['total']))
# template['confirmed']['projected']['options']['scales']['yAxes'][0]['ticks']['max'] = getUpperBound(
#     max(projData['pessimista']['total'] + projSpData['pessimista']['total']))


with open(WRITE_PATH, 'w') as f:
    json.dump(template, f)
