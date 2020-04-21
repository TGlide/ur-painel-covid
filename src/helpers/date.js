import cloneDeep from "lodash.clonedeep";

const months = [
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
];

function parseDataStr(dataStr) {
  return parseInt(
    `${months.indexOf(dataStr.slice(0, 3)) * 100 +
      parseInt(dataStr.slice(4, dataStr.length))}`
  );
}

export function sortedDateArray(arr) {
  const localeArray = cloneDeep(arr);
  return localeArray.sort((l1, l2) => {
    const l1Parsed = parseDataStr(l1);
    const l2Parsed = parseDataStr(l2);

    return l1Parsed - l2Parsed;
  });
}

export function dateToStr(dt) {
  const month = months[parseInt(dt.slice(5, 7)) - 1];
  const day = dt.slice(8, 10);
  return `${month} ${day}`;
}

export function dateCompare(a, b) {
  if (a.date > b.date) {
    return 1;
  }
  if (b.date > a.date) {
    return -1;
  }
  return 0;
}
