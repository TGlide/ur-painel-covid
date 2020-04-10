<template>
  <div class="box">
    <div class="columns box-header">
      <div class="column">
        <h4 class="title is-4">Evolução qnt. casos</h4>
      </div>
      <!-- <div class="column">
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
      </div> -->
    </div>
    <div class="columns charts">
      <div class="column is-8">
        <multi-chart
          :select-options="sources.confirmed.data"
          :default-selected="['Município']"
          select-label="Fonte Confirmados"
          :chart-data="sources.confirmed.chartData"
          :chart-options="sources.confirmed.chartOptions"
        />
      </div>
      <div class="column is-4">
        <multi-chart
          :select-options="sources.projected.data"
          :default-selected="['UERJ - Otimista']"
          select-label="Fonte Projetados (Município)"
          :chart-data="sources.projected.chartData"
          :chart-options="sources.projected.chartOptions"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { chartsJson } from "@/data/charts.js";
import MultiChart from "@/components/shared/MultiChart";
export default {
  components: { MultiChart },
  data() {
    return {
      sources: {
        confirmed: {
          data: ["Município"],
          chartData: chartsJson.confirmed.data,
          chartOptions: chartsJson.confirmed.options
        },
        projected: {
          data: Object.keys(chartsJson.projected.data.datasets),
          chartData: chartsJson.projected.data,
          chartOptions: chartsJson.projected.options
        }
      }
    };
  }
};
</script>

<style lang="scss" scoped>
@import "@/styles/theme.scss";

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

    /deep/ .multi-chart {
      flex-grow: 1;

      display: flex;
      flex-direction: column;
    }
  }
}
</style>
