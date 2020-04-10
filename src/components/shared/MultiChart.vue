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
          :key="option"
          :value="option"
          aria-role="listitem"
        >
          <span>{{ option }}</span>
        </b-dropdown-item>
      </b-dropdown>
    </b-field>
    <div class="legends" ref="legends">
      <div
        class="container"
        ref="legendsContainer"
        :style="{ transform: `translateX(${legendsContainerTranslate}px)` }"
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
      selected: [],
      legendsContainerTranslate: 0,
      legendsContainerWidth: 0
    };
  },
  computed: {
    chartDataSelected() {
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

      return data;
    },
    legends() {
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
