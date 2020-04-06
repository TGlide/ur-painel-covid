<template>
  <div class="home">
    <section class="section">
      <div class="container">
        <div class="columns">
          <div class="column is-8">
            <div class="box">
              <div class="box-header">
                <h4 class="title is-4">Evolução qnt. casos</h4>
                <b-field>
                  <p class="control">
                    <b-button class="button is-primary is-light">
                      Infectados
                    </b-button>
                  </p>
                  <p class="control">
                    <b-button class="button is-primary" outlined>
                      Hospitalizados
                    </b-button>
                  </p>
                  <p class="control">
                    <b-button class="button is-primary" outlined>
                      UTIs
                    </b-button>
                  </p>
                </b-field>
              </div>
              <div class="columns charts">
                <div class="column is-8">
                  <line-chart
                    :chartdata="charts.confirmed.data"
                    :options="charts.confirmed.options"
                    :gradientColors="confirmedGradient"
                  >
                  </line-chart>
                </div>
                <div class="column is-4">
                  <line-chart
                    :chartdata="charts.projected.data"
                    :options="charts.projected.options"
                    :gradientColors="projectedGradient"
                  >
                  </line-chart>
                </div>
              </div>
            </div>
          </div>
          <div class="column is-4">
            <div class="box stats">
              <h4 class="title is-4">Tipos de Casos</h4>
              <div class="stat">
                <span class="type"
                  ><span class="status danger" /> Total Confirmados:</span
                >
                <span class="value danger">1,068</span>
              </div>
              <div class="stat">
                <span class="type"
                  ><span class="status warning" /> Casos prováveis:</span
                >
                <span class="value warning">4,471</span>
              </div>
              <div class="stat">
                <span class="type"
                  ><span class="status gray" /> Casos fatais:</span
                >
                <span class="value gray">42</span>
              </div>
              <hr />
              <div class="stat">
                <span class="type"
                  ><span class="status blue" /> Hospitalizados:</span
                >
                <span class="value blue">253</span>
              </div>
              <div class="stat">
                <span class="type"
                  ><span class="status dark-blue" /> Em UTI:</span
                >
                <span class="value dark-blue">91</span>
              </div>
            </div>
          </div>
        </div>
        <div class="columns">
          <div class="column is-8"><div class="box"></div></div>
          <div class="column is-4"><div class="box"></div></div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import LineChart from "@/components/LineChart";

export default {
  name: "Home",
  components: { LineChart },
  data() {
    return {
      charts: {
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
            datasets: [
              {
                label: "Casos Diários",
                // backgroundColor: "rgba(255, 99, 132, 0.5)",
                borderColor: "rgb(255, 99, 132)",
                pointBackgroundColor: "rgb(255, 99, 132)",
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
                label: "Total de Casos",
                backgroundColor: "rgba(255, 99, 132, 0)",
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
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
              xAxes: [
                {
                  gridLines: {
                    display: false
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
              "Abr 13"
            ],
            datasets: [
              {
                label: "Total (Projetado)",
                // backgroundColor: "rgba(255, 99, 132, 0.5)",
                borderColor: "rgb(255, 99, 132)",
                pointBackgroundColor: "rgb(255, 99, 132)",
                data: [87, 112, 94, 120, 100, 97, 130]
              },
              {
                label: "Diário (Projetado)",
                type: "line",
                backgroundColor: "rgba(0, 0, 0, 0)",
                borderColor: "rgba(72,219,251, 0.5)",
                pointBackgroundColor: "rgba(72,219,251, 0.5)",
                data: [1197, 1309, 1403, 1523, 1623, 1720, 1850]
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
              xAxes: [
                {
                  gridLines: {
                    display: false
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
      }
    };
  },
  computed: {
    confirmedGradient() {
      return ["rgba(255, 99, 132, 0.5)", "rgba(255, 99, 132, 0.25)"];
    },
    projectedGradient() {
      return ["rgba(72,219,251, 0.5)", "rgba(72,219,251, 0.25)"];
    }
  }
};
</script>

<style lang="scss" scoped>
@import "@/styles/theme.scss";

.box {
  height: 100%;

  .box-header {
    display: flex;
    justify-content: space-between;
    align-items: center;

    margin-bottom: 2rem;

    .title {
      margin-bottom: 0 !important;
    }
  }
}

.box.stats {
  $stat-colors: (
    "danger": rgba($danger, 0.8),
    "warning": rgba($warning, 0.5),
    "gray": $gray,
    "blue": #0abde3,
    "dark-blue": #2e86de
  );

  .stat {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;

    .type {
      display: flex;
      align-items: center;
      font-size: 1.5rem;
      font-weight: 500;

      .status {
        $size: 0.5rem;
        display: inline-block;
        border-radius: 1000px;
        width: $size;
        height: $size;
        margin-right: 0.5rem;

        @each $name, $color in $stat-colors {
          &.#{$name} {
            background: $color;
          }
        }
      }
    }

    .value {
      font-size: 1.75rem;
      font-weight: 700;
      @each $name, $color in $stat-colors {
        &.#{$name} {
          color: $color;
        }
      }
    }
  }
}
</style>
