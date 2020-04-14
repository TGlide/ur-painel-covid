<template>
  <div class="box">
    <div class="columns box-header">
      <div class="column">
        <h4 class="title is-4">Locais</h4>
      </div>
      <div class="column">
        <b-field>
          <b-dropdown v-model="locales.selected" aria-role="list">
            <button
              class="button is-primary is-outlined"
              type="button"
              slot="trigger"
            >
              <span>{{ titleCase(locales.selected) }}</span>
            </button>

            <b-dropdown-item
              v-for="opt in locales.options"
              :key="opt"
              :value="opt"
              aria-role="listitem"
            >
              <span>{{ titleCase(opt) }}</span>
            </b-dropdown-item>
          </b-dropdown>
        </b-field>
      </div>
    </div>

    <b-table
      :data="sources[locales.selected]"
      default-sort-direction="desc"
      default-sort="leitos"
      sort-icon="arrow-up"
      sort-icon-size="is-small"
      paginated
      per-page="10"
      striped
    >
      <template slot-scope="props">
        <b-table-column field="ap" label="AP" sortable>
          <span v-if="props.row.ap">
            {{ props.row.ap }}
          </span>
          <span v-else>
            ?
          </span>
        </b-table-column>
        <b-table-column field="name" label="Local" width="250" sortable>
          <span v-if="props.row.name">
            {{ titleCase(props.row.name) }}
          </span>
        </b-table-column>
        <b-table-column field="infected" label="Infectados" numeric sortable>
          {{ props.row.infected }}
        </b-table-column>
        <b-table-column field="leitosSus" label="Leitos (SUS)" numeric sortable>
          {{ props.row.leitosSus }}
        </b-table-column>
        <b-table-column
          field="leitosTotal"
          label="Leitos Totais"
          numeric
          sortable
        >
          {{ props.row.leitosTotal }}
        </b-table-column>
        <b-table-column
          field="status"
          label="Farol"
          width="40"
          centered
          sortable
        >
          <div
            class="farol"
            :class="['green', 'yellow', 'red', 'none'][props.row.status - 1]"
          />
        </b-table-column>
      </template>
    </b-table>
    <p>* Leitos estimados com uma taxa de ocupação de 60%</p>
  </div>
</template>

<script>
import localStatsData from "@/data/local_stats.json";

export default {
  data() {
    return {
      locales: {
        options: [...Object.keys(localStatsData)],
        selected: "municipio"
      },
      sources: {
        ...localStatsData
      }
    };
  },

  methods: {
    titleCase(str) {
      var splitStr = str.toLowerCase().split(" ");
      for (var i = 0; i < splitStr.length; i++) {
        splitStr[i] =
          splitStr[i].charAt(0).toUpperCase() + splitStr[i].substring(1);
      }

      return splitStr.join(" ");
    }
  },
  mounted() {
    // console.log(this.sources);
    // console.log(this.sources[this.locales.selected]);
    // console.log(this.locales.options);
  }
};
</script>

<style lang="scss" scoped>
@import "@/styles/theme.scss";

.control .button {
  text-transform: capitalize;
}

.farol {
  $farol-colors: (
    "green": rgba($success, 0.75),
    "yellow": rgba($warning, 0.75),
    "red": rgba($danger, 0.75),
    "none": rgba($gray, 0.75)
  );

  $size: 1rem;
  display: inline-block;
  border-radius: 1000px;
  width: $size;
  height: $size;
  margin-right: 0.5rem;

  @each $status, $color in $farol-colors {
    &.#{$status} {
      background-color: $color;
    }
  }
}
</style>
