<template>
  <div class="about">
    <section class="section">
      <div class="container is-fluid">
        <div class="box">
          <div class="columns box-header">
            <div class="column">
              <h4 class="title is-4">Análise de Projeções</h4>
            </div>
            <div class="column">
              <b-field>
                <b-dropdown v-model="chart.selected" aria-role="list">
                  <button
                    class="button is-primary is-outlined"
                    type="button"
                    slot="trigger"
                  >
                    <span>{{ chart.options[chart.selected] }}</span>
                  </button>

                  <b-dropdown-item
                    v-for="key in Object.keys(chart.options)"
                    :key="key"
                    :value="key"
                    aria-role="listitem"
                  >
                    <span>{{ chart.options[key] }}</span>
                  </b-dropdown-item>
                </b-dropdown>
              </b-field>
            </div>
          </div>
          <div class="charts">
            <multi-chart
              v-if="!$store.getters.loading"
              :key="chart.selected"
              select-label="Tipo de Dado"
              :chart-data="combinedCharts"
              :chart-options="$store.getters.charts[chart.selected].options"
            />
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import MultiChart from "@/components/shared/MultiChart";

import cloneDeep from "lodash.clonedeep";

export default {
  components: { MultiChart },
  data() {
    return {
      chart: {
        selected: "city",
        options: {
          city: "Municipio",
          state: "Estado"
        }
      }
    };
  },
  computed: {
    combinedCharts() {
      if (this.$store.getters.loading) return undefined;
      const combined = {};
      const chartsObj = cloneDeep(
        this.$store.getters.charts[this.chart.selected]
      );
      for (let factualKey of Object.keys(chartsObj.factual)) {
        combined[`factual - ${factualKey}`] = chartsObj.factual[factualKey];
        combined[`factual - ${factualKey}`].name = `Real: ${
          combined[`factual - ${factualKey}`].name
        }`;
      }

      for (let projectedKey of Object.keys(chartsObj.projected)) {
        combined[`projected - ${projectedKey}`] =
          chartsObj.projected[projectedKey];
        combined[`projected - ${projectedKey}`].name = `Projetado: ${
          combined[`projected - ${projectedKey}`].name
        }`;
      }

      return combined;
    }
  }
};
</script>

<style lang="scss" scoped>
@import "@/styles/theme.scss";

/deep/ .box {
  height: 100%;

  .box-header {
    align-items: center;

    margin-bottom: 1rem;

    .title {
      margin-bottom: 0 !important;
    }

    .column:first-child {
      flex-grow: 1;
      flex-shrink: 0;
    }

    .column:last-child {
      &:not(:first-child) {
        flex-grow: 0;
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

    /deep/ .multi-chart {
      flex-grow: 1;

      display: flex;
      flex-direction: column;
    }
  }
}
</style>
