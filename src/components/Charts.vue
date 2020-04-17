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
    <div class="columns charts" v-if="!$store.getters.loading">
      <div class="column is-8">
        <multi-chart
          :default-selected="['cases']"
          select-label="Tipo de Dado"
          :chart-data="$store.getters.charts[mainChart.selected].factual"
          :chart-options="$store.getters.charts[mainChart.selected].options"
        />
      </div>
      <div class="column is-4">
        <multi-chart
          :default-selected="[]"
          select-label="Fonte Projetados"
          :chart-data="undefined"
          :chart-options="$store.getters.charts[mainChart.selected].options"
        />
      </div>
    </div>
  </div>
</template>

<script>
import MultiChart from "@/components/shared/MultiChart";

export default {
  components: { MultiChart },
  data() {
    return {
      mainChart: {
        selected: "city",
        options: {
          city: "Municipio",
          state: "Estado"
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
