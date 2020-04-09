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
          },
          {
            label: "Leitos (Estado)",
            backgroundColor: "rgba(0,0,0, 0)",
            borderColor: "rgba(254, 202, 87,1.0)",
            pointBackgroundColor: "rgba(254, 202, 87,1.0)",
            type: "line",
            data: [
              21319,
              21319,
              21319,
              21319,
              21319,
              21319,
              21319,
              21319,
              21319,
              21319,
              21319,
              21319,
              21319,
              21319,
              21319,
              21319,
              21319,
              21319,
              21319,
              21319,
              21319,
              21319,
              21319,
              21319,
              21319,
              21319,
              21319,
              21319,
              21319,
              21319,
              21319,
              21319
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
          },
          {
            label: "Leitos (Municipio)",
            backgroundColor: "rgba(0,0,0, 0)",
            borderColor: "rgba(254, 202, 87,1.0)",
            pointBackgroundColor: "rgba(254, 202, 87,1.0)",
            type: "line",
            data: [
              16917,
              16917,
              16917,
              16917,
              16917,
              16917,
              16917,
              16917,
              16917,
              16917,
              16917,
              16917,
              16917,
              16917,
              16917,
              16917,
              16917,
              16917,
              16917,
              16917,
              16917,
              16917,
              16917,
              16917,
              16917,
              16917,
              16917,
              16917,
              16917,
              16917,
              16917,
              16917
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
        "Abr 14",
        "Abr 15",
        "Abr 16",
        "Abr 17",
        "Abr 18"
      ],
      datasets: {
        "UERJ - Otimista": [
          {
            label: "Diário (UERJ)",
            backgroundColor: "rgba(46, 134, 222, 0.75)",
            data: [0, 48, 49, 47, 48, 48, 48, 47, 48, 48, 47, 48]
          },
          {
            label: "Total (UERJ)",
            type: "line",
            backgroundColor: "rgba(0,0,0,0)",
            borderColor: "rgba(46, 134, 222, 0.75)",
            pointBackgroundColor: "rgba(46, 134, 222, 0.75)",
            data: [
              936,
              984,
              1033,
              1080,
              1128,
              1176,
              1224,
              1271,
              1319,
              1367,
              1414,
              1462
            ]
          }
        ],
        "UERJ - Esperado": [
          {
            label: "Diário (UERJ)",
            backgroundColor: "rgba(46, 134, 222, 0.75)",
            data: [0, 51, 52, 51, 51, 51, 52, 51, 51, 52, 51, 51]
          },
          {
            label: "Total (UERJ)",
            type: "line",
            backgroundColor: "rgba(0,0,0,0)",
            borderColor: "rgba(46, 134, 222, 0.75)",
            pointBackgroundColor: "rgba(46, 134, 222, 0.75)",
            data: [
              991,
              1042,
              1094,
              1145,
              1196,
              1247,
              1299,
              1350,
              1401,
              1453,
              1504,
              1555
            ]
          }
        ],
        "UERJ - Pessimista": [
          {
            label: "Diário (UERJ)",
            backgroundColor: "rgba(46, 134, 222, 0.75)",
            data: [0, 55, 55, 54, 55, 55, 54, 55, 55, 54, 55, 55]
          },
          {
            label: "Total (UERJ)",
            type: "line",
            backgroundColor: "rgba(0,0,0,0)",
            borderColor: "rgba(46, 134, 222, 0.75)",
            pointBackgroundColor: "rgba(46, 134, 222, 0.75)",
            data: [
              1053,
              1108,
              1163,
              1217,
              1272,
              1327,
              1381,
              1436,
              1491,
              1545,
              1600,
              1655
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
