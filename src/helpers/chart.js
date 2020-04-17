import cityTemplate from "../data/charts/city_template.json";
import stateTemplate from "../data/charts/state_template.json";

function dailyDifference(list) {
  let res = [list[0]];
  for (let i = 1; i < list.length; i++) {
    res.push(list[i] - list[i - 1]);
  }

  return res;
}

export function getUpperBound(num) {
  const n_digits = Math.floor(Math.log10(num));
  return Math.ceil(num / 10 ** n_digits) * 10 ** n_digits;
}

export function getMaxValueFromDatasets(obj) {
  return Math.max(...obj.map(ds => Math.max(...ds.data)));
}

export function getCityCharts(cityData) {
  const res = { ...cityTemplate };
  const keys = Object.keys(res.factual);
  const labels = cityData.historic.map(entry => entry.date);
  const bounds = [];

  for (let key of keys) {
    res.factual[key].labels = labels;

    res.factual[key].datasets[1].data = cityData.historic.map(
      entry => entry[key]
    );
    res.factual[key].datasets[0].data = dailyDifference(
      res.factual[key].datasets[1].data
    );

    bounds.push(
      getUpperBound(getMaxValueFromDatasets(res.factual[key].datasets))
    );
  }
  bounds.push(
    getUpperBound(getMaxValueFromDatasets(res.projected.cases.datasets))
  );

  res.options.scales.yAxes[0].ticks.max = Math.max(...bounds);

  return res;
}

export function getStateCharts(stateData) {
  const res = { ...stateTemplate };
  const keys = Object.keys(res.factual);
  const labels = stateData.historic.map(entry => entry.date);
  const bounds = [];

  for (let key of keys) {
    res.factual[key].labels = labels;

    res.factual[key].datasets[1].data = stateData.historic.map(
      entry => entry[key]
    );
    res.factual[key].datasets[0].data = dailyDifference(
      res.factual[key].datasets[1].data
    );

    bounds.push(
      getUpperBound(getMaxValueFromDatasets(res.factual[key].datasets))
    );
  }
  bounds.push(
    getUpperBound(getMaxValueFromDatasets(res.projected.cases.datasets))
  );

  res.options.scales.yAxes[0].ticks.max = Math.max(...bounds);
  return res;
}
