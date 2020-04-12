<template>
  <div class="box">
    <div class="columns box-header">
      <div class="column">
        <h4 class="title is-4">Evolução qnt. casos</h4>
      </div>
      <div class="column">
        <b-field>
          <b-dropdown v-model="mainChart.selected" aria-role="list">
            <button
              class="button is-primary is-outlined"
              type="button"
              slot="trigger"
            >
              <span>{{ mainChart.options[mainChart.selected] }}</span>
            </button>

            <b-dropdown-item
              v-for="key in Object.keys(mainChart.options)"
              :key="key"
              :value="key"
              aria-role="listitem"
            >
              <span>{{ mainChart.options[key] }}</span>
            </b-dropdown-item>
          </b-dropdown>
        </b-field>
      </div>
    </div>
    <div class="columns charts">
      <div class="column is-8">
        <multi-chart
          :select-options="sources[mainChart.selected].data"
          :default-selected="['Município']"
          select-label="Fonte Confirmados"
          :chart-data="sources[mainChart.selected].chartData"
          :chart-options="sources[mainChart.selected].chartOptions"
        />
      </div>
      <div class="column is-4">
        <multi-chart
          :select-options="sources[mainChart.selected].projected.data"
          :default-selected="sources[mainChart.selected].projected.default"
          select-label="Fonte Projetados (Município)"
          :chart-data="sources[mainChart.selected].projected.chartData"
          :chart-options="sources[mainChart.selected].projected.chartOptions"
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
      mainChart: {
        selected: "confirmed",
        options: {
          confirmed: "Infectados",
          hospitalized: "Hospitalizados",
          uti: "UTI",
          fatal: "Óbitos"
        }
      },
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
          projected: {}
        },
        uti: {
          data: ["Município"],
          chartData: chartsJson.uti.data,
          chartOptions: chartsJson.uti.options,
          projected: {}
        },
        fatal: {
          data: ["Município"],
          chartData: chartsJson.fatal.data,
          chartOptions: chartsJson.fatal.options,
          projected: {}
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
