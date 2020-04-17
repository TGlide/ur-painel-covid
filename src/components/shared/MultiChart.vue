<template>
  <div class="multi-chart">
    <b-field :label="selectLabel">
      <b-dropdown v-model="selected" multiple aria-role="list">
        <button class="button is-dark" type="button" slot="trigger">
          <span>Selecionado ({{ selected.length }})</span>
          <b-icon icon="chevron-down"></b-icon>
        </button>

        <b-dropdown-item
          v-for="option in selectOptions"
          :key="option.key"
          :value="option.value"
          aria-role="listitem"
        >
          <span>{{ option.label }}</span>
        </b-dropdown-item>
      </b-dropdown>
    </b-field>

    <div class="legends" ref="legends">
      <div
        class="container"
        ref="legendsContainer"
        :style="{ transform: `translateX(${legendsContainerTranslate}%)` }"
      >
        <div class="legend" v-for="legend in legends" :key="legend.label">
          <span class="color" :style="{ backgroundColor: legend.color }" />
          <span>{{ legend.label }}</span>
        </div>
      </div>
      <div
        class="arrow"
        @click="scrollLegendsLeft"
        v-if="legendsContainerTranslate < 0"
      >
        <b-icon icon="chevron-circle-left"></b-icon>
      </div>
      <div class="arrow right" @click="scrollLegendsRight">
        <b-icon icon="chevron-circle-right"></b-icon>
      </div>
    </div>

    <line-chart
      :chartdata="chartDataSelected"
      :options="options"
      v-if="selected && selected.length > 0 && chartData"
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

import { getMaxValueFromDatasets, getUpperBound } from "@/helpers/chart.js";

export default {
  components: { LineChart, NoContent },
  props: ["selectLabel", "defaultSelected", "chartData", "chartOptions"],
  data() {
    return {
      selected: [],
      legendsContainerTranslate: 0,
      legendsContainerWidth: 0,
      options: this.chartOptions
    };
  },
  computed: {
    selectOptions() {
      if (!this.chartData) return [];
      let res = [];
      for (let key of Object.keys(this.chartData)) {
        res.push({
          value: key,
          label: this.chartData[key].name || key
        });
      }
      return res;
    },
    chartDataSelected() {
      if (!this.chartData) return undefined;

      const selectedKeys = Object.keys(this.chartData).filter(key => {
        return this.selected.includes(key);
      });

      const data = {
        labels: [],
        datasets: []
      };

      for (let key of selectedKeys) {
        data.datasets = [...data.datasets, ...this.chartData[key].datasets];
        data.labels = this.chartData[key].labels;
      }

      return data;
    },
    legends() {
      if (!this.chartData) return [];
      const res = [];

      for (let ds of this.chartDataSelected.datasets) {
        const legend = {
          label: ds.label,
          color: ds.borderColor || ds.pointBackgroundColor || ds.backgroundColor
        };

        res.push(legend);
      }
      return res;
    }
  },

  methods: {
    scrollLegendsLeft() {
      this.legendsContainerTranslate += 50;
      if (this.legendsContainerTranslate > 0)
        this.legendsContainerTranslate = 0;
    },
    scrollLegendsRight() {
      this.legendsContainerTranslate -= 50;
    }
  },
  mounted() {
    this.selected = [];
    if (this.defaultSelected) this.selected = this.defaultSelected;
  },
  watch: {
    defaultSelected: function() {
      this.selected = [];
      if (this.defaultSelected) this.selected = this.defaultSelected;
    },
    chartDataSelected: function() {
      this.options.scales.yAxes[0].ticks.max = getUpperBound(
        getMaxValueFromDatasets(this.chartDataSelected.datasets)
      );
    }
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

.legends {
  display: block;
  overflow-x: hidden;
  white-space: nowrap;

  margin-bottom: 1.25rem;
  width: 100%;

  position: relative;

  .arrow {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);

    display: flex;
    align-items: center;

    opacity: 0;
    transition: 0.5s ease;

    cursor: pointer;

    &.right {
      right: 0;
    }
  }

  &:hover {
    .arrow {
      opacity: 0.75;
    }
  }

  .container {
    transition: 0.5s ease;
  }

  .legend {
    display: inline;

    margin-right: 1rem;

    .color {
      $size: 0.5rem;
      display: inline-block;
      border-radius: 1000px;
      width: $size;
      height: $size;
      margin-right: 0.5rem;
    }
  }
}
</style>
