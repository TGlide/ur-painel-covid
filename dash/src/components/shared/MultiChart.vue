<template>
  <div class="multi-chart">
    <b-field label="Fonte Confirmados">
      <b-dropdown v-model="selected" multiple aria-role="list">
        <button class="button is-dark" type="button" slot="trigger">
          <span>Selecionado ({{ selected.length }})</span>
          <b-icon icon="chevron-down"></b-icon>
        </button>

        <b-dropdown-item
          v-for="option in selectOptions"
          :key="option"
          :value="option"
          aria-role="listitem"
        >
          <span>{{ option }}</span>
        </b-dropdown-item>
      </b-dropdown>
    </b-field>
    <line-chart
      :chartdata="chartDataSelected"
      :options="chartOptions"
      v-if="selected && selected.length > 0"
    >
    </line-chart>
    <div class="no-content-container" v-else>
      <NoContent />
    </div>
  </div>
</template>

<script>
import LineChart from "@/components/shared/LineChart";
import NoContent from "@/components/shared/NoContent";

export default {
  components: { LineChart, NoContent },
  props: [
    "selectOptions",
    "selectLabel",
    "defaultSelected",
    "chartData",
    "chartOptions"
  ],
  data() {
    return {
      selected: []
    };
  },
  computed: {
    chartDataSelected() {
      console.log(this.selectLabel, this.chartData);
      const selectedKeys = Object.keys(this.chartData.datasets).filter(key => {
        return this.selected.includes(key);
      });

      let selectedDatasets = [];
      for (let key of selectedKeys) {
        selectedDatasets = [
          ...selectedDatasets,
          ...this.chartData.datasets[key]
        ];
      }

      const data = {
        labels: this.chartData.labels,
        datasets: selectedDatasets
      };
      console.log(this.selectLabel, data);
      return data;
    }
  },
  mounted() {
    this.selected = this.defaultSelected;
  }
};
</script>

<style lang="scss">
.no-content-container {
  flex-grow: 1;

  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
