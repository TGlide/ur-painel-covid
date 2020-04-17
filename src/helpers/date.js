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
