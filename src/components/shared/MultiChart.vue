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
        class="l-container"
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
      :options="scopedCOptions"
      class="fade-in"
      :key="selected.length"
      v-if="selected && selected.length > 0 && chartData"
    >
    </line-chart>
    <div class="no-content-container" v-else>
      <NoContent />
    </div>
  </div>
</template>

<script>
import cloneDeep from "lodash.clonedeep";

import { getMaxValueFromDatasets, getUpperBound } from "@/helpers/chart.js";
import { sortedDateArray } from "@/helpers/date.js";

import LineChart from "@/components/shared/LineChart";
import NoContent from "@/components/shared/NoContent";

export default {
  components: { LineChart, NoContent },

  props: ["selectLabel", "defaultSelected", "chartData", "chartOptions"],

  data() {
    return {
      selected: [],
      legendsContainerTranslate: 0,
      legendsContainerWidth: 0,
      scopedCOptions: cloneDeep(this.chartOptions),
      scopedCData: cloneDeep(this.chartData),
      defaultMaxTick: this.chartOptions.scales.yAxes[0].ticks.max
    };
  },

  computed: {
    selectOptions() {
      if (!this.scopedCData) return [];
      let res = [];
      for (let key of Object.keys(this.scopedCData)) {
        res.push({
          value: key,
          label: this.scopedCData[key].name || key
        });
      }
      return res;
    },

    chartDataSelected() {
      if (!this.scopedCData) return undefined;

      const selectedKeys = Object.keys(this.scopedCData).filter(key => {
        return this.selected.includes(key);
      });

      let labels = new Set();

      for (let key of selectedKeys) {
        this.scopedCData[key].labels.forEach(el => labels.add(el));
      }

      labels = sortedDateArray(new Array(...labels));

      const datasets = [];
      for (let key of selectedKeys) {
        const keyDatasets = cloneDeep(this.chartData[key].datasets);
        const dsLabels = cloneDeep(this.chartData[key].labels);

        for (let idx = 0; idx < keyDatasets.length; idx++) {
          const dsData = cloneDeep(keyDatasets[idx].data);
          const newDsData = [];

          for (let label of labels) {
            const labelIndex = dsLabels.indexOf(label);
            if (labelIndex === -1) {
              newDsData.push(null);
            } else {
              newDsData.push(dsData[labelIndex]);
            }
          }

          keyDatasets[idx].data = newDsData;
        }
        datasets.push(...keyDatasets);
      }

      const data = {
        labels: new Array(...labels),
        datasets: datasets
      };

      return data;
    },

    legends() {
      if (!this.scopedCData) return [];
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

    chartOptions: function() {
      this.scopedCOptions = cloneDeep(this.chartOptions);
      this.defaultMaxTick = this.scopedCOptions.scales.yAxes[0].ticks.max;
    },

    chartDataSelected: function() {
      if (this.selected.includes("cases") || this.selected.length === 0) {
        this.scopedCOptions.scales.yAxes[0].ticks.max = this.defaultMaxTick;
      } else {
        this.scopedCOptions.scales.yAxes[0].ticks.max = getUpperBound(
          getMaxValueFromDatasets(this.chartDataSelected.datasets)
        );
      }
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

  .l-container {
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
