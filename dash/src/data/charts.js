export const chartsJson = {
  confirmed: {
    data: {
      labels: [
        "Mar 6",
        "Mar 7",
        "Mar 8",
        "Mar 9",
        "Mar 10",
        "Mar 11",
        "Mar 12",
        "Mar 13",
        "Mar 14",
        "Mar 15",
        "Mar 16",
        "Mar 17",
        "Mar 18",
        "Mar 19",
        "Mar 20",
        "Mar 21",
        "Mar 22",
        "Mar 23",
        "Mar 24",
        "Mar 25",
        "Mar 26",
        "Mar 27",
        "Mar 28",
        "Mar 29",
        "Mar 30",
        "Mar 31",
        "Abr 01",
        "Abr 02",
        "Abr 03",
        "Abr 04",
        "Abr 05",
        "Abr 06"
      ],
      datasets: {
        Estado: [
          {
            label: "Diários (Estado)",
            backgroundColor: "rgba(238, 82, 83,1.0)",
            data: [
              6,
              8,
              4,
              2,
              11,
              6,
              8,
              12,
              10,
              5,
              4,
              14,
              0,
              10,
              50,
              14,
              91,
              66,
              123,
              52,
              56,
              137,
              44,
              39,
              112,
              48,
              113,
              165,
              177,
              184,
              31,
              63
            ]
          },
          {
            label: "Total (Estado)",
            backgroundColor: "rgba(254, 202, 87, 0)",
            borderColor: "rgba(238, 82, 83,1.0)",
            pointBackgroundColor: "rgba(238, 82, 83,1.0)",
            type: "line",
            data: [
              6,
              14,
              18,
              20,
              31,
              37,
              45,
              57,
              67,
              72,
              76,
              90,
              90,
              100,
              150,
              164,
              255,
              321,
              444,
              496,
              552,
              689,
              733,
              772,
              884,
              932,
              1045,
              1210,
              1387,
              1571,
              1602,
              1665
            ]
          }
        ],
        Município: [
          {
            label: "Diários (Município)",
            backgroundColor: "rgb(255, 99, 132)",
            data: [
              4,
              5,
              3,
              1,
              8,
              4,
              5,
              8,
              4,
              6,
              3,
              9,
              0,
              3,
              31,
              9,
              67,
              44,
              64,
              53,
              37,
              63,
              58,
              26,
              38,
              30,
              114,
              110,
              60,
              115,
              86,
              42
            ]
          },
          {
            label: "Total (Município)",
            backgroundColor: "rgba(0,0,0, 0)",
            borderColor: "rgb(255, 99, 132)",
            pointBackgroundColor: "rgb(255, 99, 132)",
            type: "line",
            data: [
              4,
              9,
              12,
              13,
              21,
              25,
              30,
              38,
              42,
              48,
              51,
              60,
              60,
              63,
              94,
              103,
              170,
              214,
              278,
              331,
              368,
              431,
              489,
              515,
              553,
              583,
              697,
              807,
              867,
              982,
              1068,
              1110
            ]
          }
        ]
      }
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        xAxes: [
          {
            gridLines: {
              display: false
            },
            ticks: {
              autoSkip: true,
              maxRotation: 45,
              minRotation: 45
            }
          }
        ],
        yAxes: [
          {
            ticks: {
              max: 2000
            }
          }
        ]
      }
    }
  },
  projected: {
    data: {
      labels: [
        "Abr 07",
        "Abr 08",
        "Abr 09",
        "Abr 10",
        "Abr 11",
        "Abr 12",
        "Abr 13",
        "Abr 14"
      ],
      datasets: {
        UFRJ: [
          {
            label: "Total (UFRJ)",
            backgroundColor: "rgba(72,219,251, 0.5)",
            data: [87, 112, 94, 120, 100, 97, 130, 150]
          },
          {
            label: "Diário (UFRJ)",
            type: "line",
            backgroundColor: "rgba(0, 0, 0, 0)",
            borderColor: "rgba(72,219,251, 0.5)",
            pointBackgroundColor: "rgba(72,219,251, 0.5)",
            data: [1197, 1309, 1403, 1523, 1623, 1720, 1850, 2000]
          }
        ],
        UERJ: [
          {
            label: "Total (UERJ)",
            backgroundColor: "rgba(46, 134, 222, 0.75)",
            data: [87, 112, 94, 120, 100, 97, 130, 150]
          },
          {
            label: "Diário (UERJ)",
            type: "line",
            backgroundColor: "rgba(0,0,0,0)",
            borderColor: "rgba(46, 134, 222, 0.75)",
            pointBackgroundColor: "rgba(46, 134, 222, 0.75)",
            data: [1097, 1209, 1303, 1453, 1523, 1650, 1810, 1900]
          }
        ]
      }
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        xAxes: [
          {
            gridLines: {
              display: false
            },
            ticks: {
              autoSkip: true,
              maxRotation: 45,
              minRotation: 45
            }
          }
        ],
        yAxes: [
          {
            ticks: {
              beginAtZero: true,
              max: 2000,
              display: false
            }
          }
        ]
      }
    }
  }
};
