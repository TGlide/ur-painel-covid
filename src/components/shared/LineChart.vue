<script>
import { Bar } from "vue-chartjs";

export default {
  extends: Bar,
  props: ["chartdata", "options", "gradientColors"],
  data() {
    return {
      gradient: null
    };
  },
  mounted() {
    this.mountChart();
  },
  methods: {
    mountChart() {
      const chartData = this.chartdata;
      const chartOptions = this.options;

      this.gradient = this.$refs.canvas
        .getContext("2d")
        .createLinearGradient(0, 0, 0, 450);
      if (this.gradientColors) {
        for (let idx = 0; idx < this.gradientColors.length; idx++) {
          this.gradient.addColorStop(idx, this.gradientColors[idx]);
        }
        for (let dsIdx = 0; dsIdx < chartData.datasets.length; dsIdx++) {
          if (
            !(
              chartData.datasets[dsIdx].type &&
              chartData.datasets[dsIdx].type === "line"
            )
          )
            chartData.datasets[dsIdx].backgroundColor = this.gradient;
        }
      }

      this.renderChart(chartData, chartOptions);
    }
  },
  watch: {
    chartdata() {
      this.mountChart();
    }
  }
};
</script>

<style></style>
