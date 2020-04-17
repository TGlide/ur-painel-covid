import aps from "../data/ap.json";
import leitos from "../data/leitos.json";

const BED_OCCUPATION_RATE = 0.6;
const BED_RETENTION_RATE = 1 - BED_OCCUPATION_RATE;

function getStatus(cases, leitos) {
  if (cases > leitos * 0.749) return 3;
  if (cases > leitos * 0.49) return 2;
  return 1;
}

function localeArrayToObject(neighborhoods) {
  const res = {};

  for (let n of neighborhoods) {
    res[
      n.name
        .toLowerCase()
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
    ] = {
      cases: n.cases,
      dead: n.dead
    };
  }

  return res;
}

export function getLocaleData(neighborhoods, cities) {
  const neighborhoodsObj = localeArrayToObject(neighborhoods);
  const citiesObj = localeArrayToObject(cities);
  let res = {
    estado: [],
    municipio: [],
    aps: []
  };

  for (let [key, entry] of Object.entries(leitos.estado)) {
    res.estado.push({
      name: key,
      cases: citiesObj[key.toLowerCase()]
        ? citiesObj[key.toLowerCase()].cases
        : 0,
      leitosTotal: Math.round(entry.UTI * BED_RETENTION_RATE),
      leitosSus: Math.round(entry.UTI_SUS * BED_RETENTION_RATE),
      status: getStatus(
        citiesObj[key.toLowerCase()] ? citiesObj[key.toLowerCase()].cases : 0,
        entry.UTI * BED_RETENTION_RATE
      )
    });
  }

  const ap_relation = {};
  for (let [bairro, ap] of Object.entries(aps)) {
    ap_relation[ap] = [bairro, ...(ap_relation[ap] || [])];
    if (Object.keys(leitos.municipio).includes(bairro))
      leitos.municipio[bairro].ap = ap;
  }

  const ap_index = {};
  for (let [ap, bairros] of Object.entries(ap_relation)) {
    let ap_entry = {
      ap: ap,
      cases: 0,
      leitosSus: 0,
      leitosTotal: 0
    };

    for (let bairro of bairros) {
      let bairro_obj = leitos.municipio[bairro] || {};
      if (Object.keys(bairro_obj).length === 0) continue;

      ap_entry.cases += neighborhoodsObj[bairro]
        ? neighborhoodsObj[bairro].cases
        : 0;
      ap_entry.leitosSus += Math.round(bairro_obj.UTI_SUS * BED_RETENTION_RATE);
      ap_entry.leitosTotal += Math.round(bairro_obj.UTI * BED_RETENTION_RATE);
    }

    ap_entry.status = getStatus(ap_entry.cases, ap_entry.leitosTotal);

    res.aps.push(ap_entry);
    ap_index[ap] = ap_entry;
  }

  for (let [b_name, b_entry] of Object.entries(leitos.municipio)) {
    let mun_entry = {
      ap: b_entry.ap || "",
      name: b_name,
      cases: neighborhoodsObj[b_name] ? neighborhoodsObj[b_name].cases : 0,
      leitosSus: Math.round(b_entry["UTI_SUS"] * BED_RETENTION_RATE),
      leitosTotal: Math.round(b_entry["UTI"] * BED_RETENTION_RATE)
    };

    if (mun_entry["ap"]) {
      const ap = ap_index[mun_entry["ap"]];
      mun_entry["status"] = getStatus(ap["cases"], ap["leitosTotal"]);
    } else mun_entry["status"] = 4;

    res["municipio"].push(mun_entry);
  }

  return res;
}
