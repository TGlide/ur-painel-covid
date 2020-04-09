<template>
  <div class="box stats">
    <h4 class="title is-4">Tipos de Casos</h4>

    <br />
    <h5 class="title is-5">Estado</h5>
    <div class="stat">
      <span class="type"
        ><span class="status danger" /> Total Confirmados:</span
      >
      <span class="value danger">{{ this.confirmed }}</span>
    </div>
    <div class="stat">
      <span class="type"><span class="status warning" /> Casos prováveis:</span>
      <span class="value warning">4,471</span>
    </div>
    <div class="stat">
      <span class="type"><span class="status gray" /> Casos fatais:</span>
      <span class="value gray">{{ this.fatal }}</span>
    </div>

    <div class="stat">
      <span class="type"><span class="status blue" /> Hospitalizados:</span>
      <span class="value blue">253</span>
    </div>
    <div class="stat">
      <span class="type"><span class="status dark-blue" /> Em UTI:</span>
      <span class="value dark-blue">91</span>
    </div>

    <br />
    <hr />
    <br />

    <h5 class="title is-5">Município</h5>
    <div class="stat">
      <span class="type"
        ><span class="status danger" /> Total Confirmados:</span
      >
      <span class="value danger">{{ this.confirmed }}</span>
    </div>
    <div class="stat">
      <span class="type"><span class="status warning" /> Casos prováveis:</span>
      <span class="value warning">4,471</span>
    </div>
    <div class="stat">
      <span class="type"><span class="status gray" /> Casos fatais:</span>
      <span class="value gray">{{ this.fatal }}</span>
    </div>
    <div class="stat">
      <span class="type"><span class="status blue" /> Hospitalizados:</span>
      <span class="value blue">253</span>
    </div>
    <div class="stat">
      <span class="type"><span class="status dark-blue" /> Em UTI:</span>
      <span class="value dark-blue">91</span>
    </div>
  </div>
</template>

<script>
import infectedJson from "@/data/infected.json";
export default {
  data() {
    return {
      confirmed: 0,
      fatal: 0
    };
  },
  mounted() {
    for (let a of Object.entries(infectedJson)) {
      this.confirmed += a[1].confirmed;
      this.fatal += parseInt(a[1].dead);
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
