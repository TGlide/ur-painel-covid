<template>
  <div class="box stats">
    <div class="columns box-header">
      <div class="column">
        <h4 class="title is-4">Tipos de Casos</h4>
      </div>
      <!-- <div class="column">
        <b-field>
          <p class="control" v-for="locale in locales" :key="locale">
            <b-button
              class="button is-primary"
              @click="selected = locale"
              :outlined="selected != locale"
            >
              {{ locale }}
            </b-button>
          </p>
        </b-field>
      </div> -->
    </div>
    <div class="stat">
      <span class="type"
        ><span class="status danger" /> Total Confirmados:</span
      >
      <span class="value danger">{{ sources.confirmed }}</span>
    </div>
    <!-- <div class="stat">
      <span class="type"><span class="status warning" /> Casos prováveis:</span>
      <span class="value warning">4,471</span>
    </div> -->
    <div class="stat">
      <span class="type"><span class="status gray" /> Casos fatais:</span>
      <span class="value gray">{{ sources.fatal }}</span>
    </div>

    <div class="stat">
      <span class="type"><span class="status blue" /> Hospitalizados:</span>
      <span class="value blue">{{ sources.hospitalized }}</span>
    </div>
    <div class="stat">
      <span class="type"><span class="status dark-blue" /> Em UTI:</span>
      <span class="value dark-blue">{{ sources.uti }}</span>
    </div>
  </div>
</template>

<script>
// import infectedJson from "@/data/infected.json";
import chartsJson from "@/data/charts.json";

export default {
  data() {
    return {
      locales: ["Município", "Estado"],
      selected: "Município",
      sources: {
        confirmed: 0,
        fatal: 0,
        hospitalized: 0,
        uti: 0
      }
    };
  },
  mounted() {
    for (let key of Object.keys(this.sources)) {
      const chartData = chartsJson[key].data.datasets[this.selected][1].data;
      this.sources[key] = chartData[chartData.length - 1];
    }
  }
};
</script>

<style lang="scss" scoped>
@import "@/styles/theme.scss";

.stats {
  $stat-colors: (
    "danger": rgba($danger, 0.8),
    "warning": rgba($warning, 0.5),
    "gray": $gray,
    "blue": #0abde3,
    "dark-blue": #2e86de
  );

  .stat {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;

    .type {
      display: flex;
      align-items: center;
      font-size: 1.5rem;
      font-weight: 500;

      .status {
        $size: 0.5rem;
        display: inline-block;
        border-radius: 1000px;
        width: $size;
        height: $size;
        margin-right: 0.5rem;

        @each $name, $color in $stat-colors {
          &.#{$name} {
            background: $color;
          }
        }
      }
    }

    .value {
      font-size: 1.75rem;
      font-weight: 700;
      @each $name, $color in $stat-colors {
        &.#{$name} {
          color: $color;
        }
      }
    }
  }
}
</style>
