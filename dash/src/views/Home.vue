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
          <div class="column is-7">
            <div class="box"></div>
          </div>

          <div class="column is-5">
            <div class="box">
              <h4 class="title is-4">Bairros</h4>
              <b-table
                :data="neighborhoods.data"
                default-sort-direction="desc"
                default-sort="leitos"
                sort-icon="arrow-up"
                sort-icon-size="is-small"
              >
                <template slot-scope="props">
                  <b-table-column
                    field="name"
                    label="Bairro"
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
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import chartsJson from "@/data/charts.json";

import LineChart from "@/components/LineChart";

export default {
  name: "Home",
  components: { LineChart },
  data() {
    return {
      charts: { ...chartsJson },
      neighborhoods: {
        data: [
          { name: "Barra Da Tijuca", infected: 118, leitos: 500, status: 1 },
          { name: "Copacabana", infected: 174, leitos: 200, status: 2 },
          { name: "Leblon", infected: 71, leitos: 50, status: 3 },
          { name: "Ipanema", infected: 58, leitos: 300, status: 1 },
          { name: "Botafogo", infected: 51, leitos: 150, status: 1 },
          { name: "Tijuca", infected: 40, leitos: 100, status: 1 }
        ]
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
