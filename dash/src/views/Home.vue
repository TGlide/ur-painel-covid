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
              "Feb 15",
              "Feb 16",
              "Feb 17",
              "Feb 18",
              "Feb 19",
              "Feb 20",
              "Feb 21",
              "Feb 22",
              "Feb 23",
              "Feb 24",
              "Feb 25",
              "Feb 26",
              "Feb 27",
              "Feb 28",
              "Feb 29",
              "Mar 1",
              "Mar 2",
              "Mar 3",
              "Mar 4",
              "Mar 5",
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
              "Mar 26"
            ],
            datasets: [
              {
                label: "Total de Casos (Confirmados)",
                // backgroundColor: "rgba(255, 99, 132, 0.5)",
                borderColor: "rgb(255, 99, 132)",
                pointBackgroundColor: "rgb(255, 99, 132)",
                data: [
                  15,
                  15,
                  15,
                  15,
                  15,
                  15,
                  35,
                  35,
                  35,
                  53,
                  57,
                  60,
                  60,
                  63,
                  68,
                  75,
                  100,
                  124,
                  158,
                  221,
                  319,
                  435,
                  541,
                  704,
                  994,
                  1301,
                  1630,
                  2183,
                  2770,
                  3613,
                  4596,
                  6344,
                  9197,
                  13779,
                  19367,
                  24192,
                  33592,
                  43781,
                  54856,
                  68211,
                  85435
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
                    max: 300000
                  }
                }
              ]
            }
          }
        },
        projected: {
          data: {
            labels: [
              "Mar 27",
              "Mar 28",
              "Mar 29",
              "Mar 30",
              "Mar 31",
              "Abr 01",
              "Abr 02"
            ],
            datasets: [
              {
                label: "Total de Casos (Projetados)",
                // backgroundColor: "rgba(255, 99, 132, 0.5)",
                borderColor: "rgb(255, 99, 132)",
                pointBackgroundColor: "rgb(255, 99, 132)",
                data: [113645, 132033, 154550, 183200, 221342, 252012, 290123]
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
                    max: 300000,
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
