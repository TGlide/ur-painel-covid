import os
import re
import math
import json
import pandas as pd

from pandas import ExcelWriter
from pandas import ExcelFile
from pprint import pprint as pp
from unidecode import unidecode


BED_OCCUPATION_RATE = 0.6
BED_RETENTION_RATE = 1 - BED_OCCUPATION_RATE


def getStatus(infected, leitos):
    if infected > leitos * 0.749:
        # print(f"I:{infected}\tL: {leitos}\tR: 3")
        return 3
    if infected > leitos * 0.49:
        # print(infected, leitos, 2)
        return 2
    # print(infected, leitos, 1)
    return 1


def clean_string(s):
    return unidecode(s.lower())


infected_path = os.path.join(
    os.getcwd(), "scrapper", "files", "in", "infected.json")
aps_path = os.path.join(
    os.getcwd(), "scrapper", "files", "out", "ap.json")
leitos_path = os.path.join(
    os.getcwd(), "scrapper", "files", "out", "leitos.json")
write_path = os.path.join(
    os.getcwd(), "src", "data",  "local_stats.json")

f = open(infected_path, 'r')
infected = json.load(f)
f.close()

f = open(aps_path, 'r')
aps = json.load(f)
f.close()

f = open(leitos_path, 'r')
leitos = json.load(f)
f.close()


res = {
    "estado": [],
    "municipio": [],
    "aps": []
}


# State data
res["estado"] = [
    {
        "name": key,
        "infected": 0,
        "leitosSus": round(entry['UTI_SUS'] * BED_RETENTION_RATE),
        "leitosTotal": round(entry['UTI'] * BED_RETENTION_RATE),
        "status": getStatus(entry['Total'], entry['UTI'] * BED_RETENTION_RATE)
    }
    for key, entry in leitos['estado'].items()
]

# AP data
ap_relation = {}

for bairro, ap in aps.items():
    ap_relation[ap] = [bairro] + ap_relation.get(ap, [])
    if leitos["municipio"].get(clean_string(bairro).upper()):
        leitos["municipio"][clean_string(bairro).upper()]["ap"] = ap


ap_index = {}
for ap, bairros in ap_relation.items():
    ap_entry = {
        "ap": ap,
        "infected": 0,
        "leitosSus": 0,
        "leitosTotal": 0
    }

    for bairro in bairros:
        bairro_up = clean_string(bairro).upper()
        bairro_obj = leitos['municipio'].get(bairro_up, {})
        if not bairro_obj:
            continue

        ap_entry['infected'] += infected.get(bairro_up, {}).get('confirmed', 0)
        ap_entry['leitosSus'] += round(bairro_obj['UTI_SUS']
                                       * BED_RETENTION_RATE)
        ap_entry['leitosTotal'] += round(bairro_obj['UTI']
                                         * BED_RETENTION_RATE)

    ap_entry['status'] = getStatus(
        ap_entry['infected'], ap_entry['leitosTotal'])

    res['aps'].append(ap_entry)
    ap_index[ap] = ap_entry

for b_name, b_entry in leitos['municipio'].items():
    mun_entry = {
        "ap": b_entry.get("ap", ""),
        "name": clean_string(b_name),
        "infected": infected.get(clean_string(b_name).upper(), {}).get('confirmed', 0),
        "leitosSus": round(b_entry['UTI_SUS'] * BED_RETENTION_RATE),
        "leitosTotal": round(b_entry['UTI'] * BED_RETENTION_RATE),
    }
    if mun_entry['ap']:
        ap = ap_index[mun_entry["ap"]]
        mun_entry['status'] = getStatus(ap["infected"], ap["leitosTotal"])
    else:
        mun_entry['status'] = 4

    res["municipio"].append(mun_entry)

with open(write_path, 'w') as f:
    json.dump(res, f)
