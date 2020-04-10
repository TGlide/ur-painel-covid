<template>
  <div class="box">
    <div class="columns box-header">
      <div class="column">
        <h4 class="title is-4">Evolução qnt. casos</h4>
      </div>
      <div class="column">
        <b-field>
          <p class="control">
            <b-button
              class="button is-primary is-light"
              :outlined="mainChartSelection !== 'confirmed'"
              @click="mainChartSelection = 'confirmed'"
            >
              Infectados
            </b-button>
          </p>
          <p class="control">
            <b-button
              class="button is-primary"
              :outlined="mainChartSelection !== 'hospitalized'"
              @click="mainChartSelection = 'hospitalized'"
            >
              Hospitalizados
            </b-button>
          </p>
          <p class="control">
            <b-button
              class="button is-primary"
              :outlined="mainChartSelection !== 'uti'"
              @click="mainChartSelection = 'uti'"
            >
              UTIs
            </b-button>
          </p>
          <p class="control">
            <b-button
              class="button is-primary"
              :outlined="mainChartSelection !== 'fatal'"
              @click="mainChartSelection = 'fatal'"
            >
              Óbitos
            </b-button>
          </p>
        </b-field>
      </div>
    </div>
    <div class="columns charts">
      <div class="column is-8">
        <multi-chart
          :select-options="sources[mainChartSelection].data"
          :default-selected="['Município']"
          select-label="Fonte Confirmados"
          :chart-data="sources[mainChartSelection].chartData"
          :chart-options="sources[mainChartSelection].chartOptions"
        />
      </div>
      <div class="column is-4">
        <multi-chart
          :select-options="sources[mainChartSelection].projected.data"
          :default-selected="sources[mainChartSelection].projected.default"
          select-label="Fonte Projetados (Município)"
          :chart-data="sources[mainChartSelection].projected.chartData"
          :chart-options="sources[mainChartSelection].projected.chartOptions"
        />
      </div>
    </div>
  </div>
</template>

<script>
import chartsJson from "@/data/charts.json";
import MultiChart from "@/components/shared/MultiChart";

export default {
  components: { MultiChart },
  data() {
    return {
      mainChartSelection: "confirmed",
      sources: {
        confirmed: {
          data: ["Município"],
          chartData: chartsJson.confirmed.data,
          chartOptions: chartsJson.confirmed.options,
          projected: {
            default: [
              Object.keys(chartsJson.confirmed.projected.data.datasets)[0]
            ],
            data: Object.keys(chartsJson.confirmed.projected.data.datasets),
            chartData: chartsJson.confirmed.projected.data,
            chartOptions: chartsJson.confirmed.projected.options
          }
        },
        hospitalized: {
          data: ["Município"],
          chartData: chartsJson.hospitalized.data,
          chartOptions: chartsJson.hospitalized.options,
          projected: {
            default: [],
            data: [],
            chartData: undefined,
            chartOptions: undefined
          }
        },
        uti: {
          data: ["Município"],
          chartData: chartsJson.uti.data,
          chartOptions: chartsJson.uti.options,
          projected: {
            default: [],
            data: undefined,
            chartData: undefined,
            chartOptions: undefined
          }
        },
        fatal: {
          data: ["Município"],
          chartData: chartsJson.fatal.data,
          chartOptions: chartsJson.fatal.options,
          projected: {
            default: [],
            data: undefined,
            chartData: undefined,
            chartOptions: undefined
          }
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
