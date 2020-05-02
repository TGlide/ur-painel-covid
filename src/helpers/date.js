import cloneDeep from "lodash.clonedeep";
import { ptBR } from "date-fns/locale";
import { format as formatDate, parse as parseDate } from "date-fns";

export function dateToStr(dt) {
  const formattedDate = formatDate(new Date(dt), "MMM dd", { locale: ptBR });
  return `${formattedDate.slice(0, 1).toUpperCase()}${formattedDate.slice(1)}`;
}

function parseDateStr(dateStr) {
  const dateObj = parseDate(dateStr.toLowerCase(), "MMM dd", new Date(), {
    locale: ptBR
  });

  return dateObj;
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

export function sortedDateArray(arr) {
  const localeArray = cloneDeep(arr);
  return localeArray.sort((l1, l2) => {
    const l1Parsed = parseDateStr(l1);
    const l2Parsed = parseDateStr(l2);

    return l1Parsed - l2Parsed;
  });
}
