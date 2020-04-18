<template>
  <div class="box stats">
    <div class="columns box-header">
      <div class="column">
        <h4 class="title is-4">Tipos de Casos</h4>
      </div>
      <div class="column">
        <b-field>
          <b-dropdown v-model="selected" aria-role="list">
            <button
              class="button is-primary is-outlined"
              type="button"
              slot="trigger"
            >
              <span>{{ locales[selected] }}</span>
            </button>

            <b-dropdown-item
              v-for="key in Object.keys(locales)"
              :key="key"
              :value="key"
              aria-role="listitem"
            >
              <span>{{ locales[key] }}</span>
            </b-dropdown-item>
          </b-dropdown>
        </b-field>
      </div>
    </div>
    <div class="stat">
      <span class="type"
        ><span class="status danger" /> Total Confirmados:</span
      >
      <span class="value danger">{{
        $store.getters[selected].current.cases || "-"
      }}</span>
    </div>
    <div class="stat">
      <span class="type"><span class="status gray" /> Casos fatais:</span>
      <span class="value gray">{{
        $store.getters[selected].current.dead || "-"
      }}</span>
    </div>

    <div class="stat">
      <span class="type"><span class="status blue" /> Hospitalizados:</span>
      <span class="value blue">{{
        $store.getters[selected].current.hospitalized || "-"
      }}</span>
    </div>
    <div class="stat">
      <span class="type"><span class="status dark-blue" /> Em UTI:</span>
      <span class="value dark-blue">{{
        $store.getters[selected].current.uti || "-"
      }}</span>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      locales: { city: "Município", state: "Estado" },
      selected: "city"
    };
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
