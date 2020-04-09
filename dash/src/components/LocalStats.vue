<template>
  <div class="box">
    <h4 class="title is-4">Locais</h4>
    <b-table
      :data="neighborhoods.data"
      default-sort-direction="desc"
      default-sort="leitos"
      sort-icon="arrow-up"
      sort-icon-size="is-small"
      paginated
      per-page="20"
      striped
    >
      <template slot-scope="props">
        <b-table-column field="name" label="Local" width="250" sortable>
          {{ props.row.name }}
        </b-table-column>
        <b-table-column field="infected" label="Infectados" numeric sortable>
          {{ props.row.infected }}
        </b-table-column>
        <b-table-column field="leitos" label="Leitos" numeric sortable>
          {{ props.row.leitos }}
        </b-table-column>

        <b-table-column
          field="status"
          label="Faról"
          width="40"
          centered
          sortable
        >
          <div
            class="farol"
            :class="['green', 'yellow', 'red'][props.row.status - 1]"
          />
        </b-table-column>
      </template>
    </b-table>
  </div>
</template>

<script>
import leitosJson from "@/data/leitos.json";
import infectedJson from "@/data/infected.json";

export default {
  data() {
    return {
      neighborhoods: {
        data: []
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
    this.neighborhoods.data = Object.entries(leitosJson.municipio).map(n => {
      let res = {
        name: this.titleCase(n[0].toLowerCase()),
        leitos: n[1],
        infected: Object.keys(infectedJson).includes(n[0].toUpperCase())
          ? infectedJson[n[0].toUpperCase()].confirmed
          : 0
      };
      if (res.infected >= res.leitos * 0.75) {
        res.status = 3;
      } else if (res.infected >= res.leitos * 0.5) {
        res.status = 2;
      } else {
        res.status = 1;
      }
      return res;
    });
  }
};
</script>

<style lang="scss" scoped>
@import "@/styles/theme.scss";

.farol {
  $farol-colors: (
    "green": rgba($success, 0.75),
    "yellow": rgba($warning, 0.75),
    "red": rgba($danger, 0.75)
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
