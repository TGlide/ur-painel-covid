import { dateToStr } from "./date";

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

export function getCharts(receivedData, projections, type) {
  const template = type == "city" ? cityTemplate : stateTemplate;
  const res = { ...template };
  const keys = Object.keys(res.factual);
  const labels = receivedData.historic.map(entry => entry.date);
  const bounds = [];

  for (let key of keys) {
    res.factual[key].labels = labels;

    res.factual[key].datasets[1].data = receivedData.historic.map(
      entry => entry[key]
    );
    res.factual[key].datasets[0].data = dailyDifference(
      res.factual[key].datasets[1].data
    );

    bounds.push(
      getUpperBound(getMaxValueFromDatasets(res.factual[key].datasets))
    );
  }

  const projection_keys_started = {
    cases: false,
    leitos: false
  };

  for (let projection of projections) {
    for (let key of Object.keys(projection_keys_started)) {
      if (projection[key] > 0) projection_keys_started[key] = true;

      if (projection_keys_started[key]) {
        res.projected[key].labels.push(dateToStr(projection.date));
        res.projected[key].datasets[1].data.push(projection[key]);
        const total_length = res.projected[key].datasets[1].data.length;
        res.projected[key].datasets[0].data.push(
          total_length > 1
            ? res.projected[key].datasets[1].data[total_length - 1] -
                res.projected[key].datasets[1].data[total_length - 2]
            : 0
        );
      }
    }
  }

  bounds.push(
    getUpperBound(getMaxValueFromDatasets(res.projected.cases.datasets))
  );

  res.options.scales.yAxes[0].ticks.max = Math.max(...bounds);

  return res;
}
