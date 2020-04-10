<template>
  <div class="box">
    <div class="columns box-header">
      <div class="column">
        <h4 class="title is-4">Locais</h4>
      </div>
      <!-- <div class="column">
        <b-field>
          <p
            class="control"
            v-for="locale in Object.keys(locales)"
            :key="locale"
          >
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

    <b-table
      :data="locales[selected].data"
      default-sort-direction="desc"
      default-sort="leitos"
      sort-icon="arrow-up"
      sort-icon-size="is-small"
      paginated
      per-page="10"
      striped
    >
      <template slot-scope="props">
        <b-table-column field="name" label="Local" width="250" sortable>
          {{ props.row.name }}
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
    <p>* Leitos estimados com uma taxa de ocupação de 60%</p>
  </div>
</template>

<script>
import leitosJson from "@/data/leitos.json";
import infectedJson from "@/data/infected.json";

export default {
  data() {
    return {
      locales: {
        municipio: {
          data: []
        },
        estado: {
          data: []
        }
      },
      selected: "municipio"
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
    for (let key of Object.keys(this.locales)) {
      this.locales[key].data = Object.entries(leitosJson[key]).map(n => {
        let res = {
          name: this.titleCase(n[0].toLowerCase()),
          leitosSus: Math.ceil(n[1].UTI_SUS * 0.4),
          leitosTotal: Math.ceil(n[1].UTI * 0.4),
          infected: Object.keys(infectedJson).includes(n[0].toUpperCase())
            ? infectedJson[n[0].toUpperCase()].confirmed
            : 0
        };
        if (res.infected >= res.leitosTotal * 0.75) {
          res.status = 3;
        } else if (res.infected >= res.leitosTotal * 0.5) {
          res.status = 2;
        } else {
          res.status = 1;
        }
        return res;
      });
    }
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
