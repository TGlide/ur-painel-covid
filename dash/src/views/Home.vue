<template>
  <div class="home">
    <section class="section">
      <div class="container">
        <div class="columns">
          <!-- Charts -->
          <div class="column is-12">
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
                  <b-field label="Fonte Confirmados">
                    <b-dropdown
                      v-model="sources.confirmed.selected"
                      multiple
                      aria-role="list"
                    >
                      <button
                        class="button is-dark"
                        type="button"
                        slot="trigger"
                      >
                        <span
                          >Selecionado ({{
                            sources.confirmed.selected.length
                          }})</span
                        >
                        <b-icon icon="chevron-down"></b-icon>
                      </button>

                      <b-dropdown-item
                        v-for="option in sources.confirmed.data"
                        :key="option"
                        :value="option"
                        aria-role="listitem"
                      >
                        <span>{{ option }}</span>
                      </b-dropdown-item>
                    </b-dropdown>
                  </b-field>
                  <line-chart
                    :chartdata="charts.confirmed.data"
                    :options="charts.confirmed.options"
                    v-if="
                      sources.confirmed.selected &&
                        sources.confirmed.selected.length > 0
                    "
                  >
                  </line-chart>
                  <NoContent v-else />
                </div>
                <div class="column is-4">
                  <b-field label="Fonte Projetados (Município)">
                    <b-dropdown
                      v-model="sources.projected.selected"
                      multiple
                      aria-role="list"
                    >
                      <button
                        class="button is-dark"
                        type="button"
                        slot="trigger"
                      >
                        <span
                          >Selecionado ({{
                            sources.projected.selected.length
                          }})</span
                        >
                        <b-icon icon="chevron-down"></b-icon>
                      </button>

                      <b-dropdown-item
                        v-for="option in sources.projected.data"
                        :key="option"
                        :value="option"
                        aria-role="listitem"
                      >
                        <span>{{ option }}</span>
                      </b-dropdown-item>
                    </b-dropdown>
                  </b-field>

                  <line-chart
                    :chartdata="charts.projected.data"
                    :options="charts.projected.options"
                    v-if="
                      sources.projected.selected &&
                        sources.projected.selected.length > 0
                    "
                  >
                  </line-chart>
                  <NoContent v-else />
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="columns">
          <!-- Neighborhoods -->
          <div class="column is-7">
            <div class="box">
              <h4 class="title is-4">Locais</h4>
              <b-table
                :data="neighborhoods.data"
                default-sort-direction="desc"
                default-sort="leitos"
                sort-icon="arrow-up"
                sort-icon-size="is-small"
                paginated
                per-page="20"
                striped
              >
                <template slot-scope="props">
                  <b-table-column
                    field="name"
                    label="Local"
                    width="250"
                    sortable
                  >
                    {{ props.row.name }}
                  </b-table-column>
                  <b-table-column
                    field="infected"
                    label="Infectados"
                    numeric
                    sortable
                  >
                    {{ props.row.infected }}
                  </b-table-column>
                  <b-table-column
                    field="leitos"
                    label="Leitos"
                    numeric
                    sortable
                  >
                    {{ props.row.leitos }}
                  </b-table-column>

                  <b-table-column
                    field="status"
                    label="Faról"
                    width="40"
                    centered
                    sortable
                  >
                    <div
                      class="farol"
                      :class="['green', 'yellow', 'red'][props.row.status - 1]"
                    />
                  </b-table-column>
                </template>
              </b-table>
            </div>
          </div>
          <!-- Stats -->
          <div class="column is-5">
            <div class="box stats">
              <h4 class="title is-4">Tipos de Casos</h4>

              <br />
              <h5 class="title is-5">Estado</h5>
              <div class="stat">
                <span class="type"
                  ><span class="status danger" /> Total Confirmados:</span
                >
                <span class="value danger">{{ this.confirmed }}</span>
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
                <span class="value gray">{{ this.fatal }}</span>
              </div>

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

              <br />
              <hr />
              <br />

              <h5 class="title is-5">Município</h5>
              <div class="stat">
                <span class="type"
                  ><span class="status danger" /> Total Confirmados:</span
                >
                <span class="value danger">{{ this.confirmed }}</span>
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
                <span class="value gray">{{ this.fatal }}</span>
              </div>
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
      </div>
    </section>
  </div>
</template>

<script>
import { chartsJson } from "@/data/charts.js";
import leitosJson from "@/data/leitos.json";
import infectedJson from "@/data/infected.json";

import LineChart from "@/components/LineChart";
import NoContent from "@/components/NoContent";

export default {
  name: "Home",
  components: { LineChart, NoContent },
  data() {
    return {
      neighborhoods: {
        data: []
      },
      sources: {
        confirmed: {
          selected: ["Estado", "Município"],
          data: ["Estado", "Município"]
        },
        projected: {
          selected: ["UFRJ"],
          data: ["UFRJ", "UERJ", "UFF", "PUC"]
        }
      },
      confirmed: 0,
      fatal: 0
    };
  },
  computed: {
    charts() {
      const confirmedKeys = Object.keys(
        chartsJson.confirmed.data.datasets
      ).filter(key => {
        return this.sources.confirmed.selected.includes(key);
      });

      let confirmedDatasets = [];
      for (let key of confirmedKeys) {
        confirmedDatasets = [
          ...confirmedDatasets,
          ...chartsJson.confirmed.data.datasets[key]
        ];
      }

      const projectedKeys = Object.keys(
        chartsJson.projected.data.datasets
      ).filter(key => {
        return this.sources.projected.selected.includes(key);
      });

      let projectedDatasets = [];
      for (let key of projectedKeys) {
        projectedDatasets = [
          ...projectedDatasets,
          ...chartsJson.projected.data.datasets[key]
        ];
      }

      const res = {
        confirmed: {
          data: {
            labels: chartsJson.confirmed.data.labels,
            datasets: confirmedDatasets
          },
          options: chartsJson.confirmed.options
        },
        projected: {
          data: {
            labels: chartsJson.projected.data.labels,
            datasets: projectedDatasets
          },
          options: chartsJson.projected.options
        }
      };
      console.log(res);
      return res;
    }
  },
  methods: {
    titleCase(str) {
      var splitStr = str.toLowerCase().split(" ");
      for (var i = 0; i < splitStr.length; i++) {
        splitStr[i] =
          splitStr[i].charAt(0).toUpperCase() + splitStr[i].substring(1);
      }

      return splitStr.join(" ");
    }
  },
  mounted() {
    this.neighborhoods.data = Object.entries(leitosJson.municipio).map(n => {
      console.log(n);
      let res = {
        name: this.titleCase(n[0].toLowerCase()),
        leitos: n[1],
        infected: Object.keys(infectedJson).includes(n[0].toUpperCase())
          ? infectedJson[n[0].toUpperCase()].confirmed
          : 0
      };
      if (res.infected >= res.leitos * 0.75) {
        res.status = 3;
      } else if (res.infected >= res.leitos * 0.5) {
        res.status = 2;
      } else {
        res.status = 1;
      }
      return res;
    });

    for (let a of Object.entries(infectedJson)) {
      this.confirmed += a[1].confirmed;
      this.fatal += parseInt(a[1].dead);
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

.stats {
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

.charts {
  align-items: stretch;

  /deep/ .dropdown button {
    border-color: $white;
    &:hover,
    &:active,
    &:focus {
      border-color: $white;
    }
  }

  .column {
    display: flex;
    flex-direction: column;
    /deep/ .no-content {
      flex-grow: 1;
    }
  }
}

.farol {
  $farol-colors: (
    "green": rgba($success, 0.75),
    "yellow": rgba($warning, 0.75),
    "red": rgba($danger, 0.75)
  );

  $size: 1rem;
  display: inline-block;
  border-radius: 1000px;
  width: $size;
  height: $size;
  margin-right: 0.5rem;

  @each $status, $color in $farol-colors {
    &.#{$status} {
      background-color: $color;
    }
  }
}
</style>
