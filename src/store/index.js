import Vue from "vue";
import Vuex from "vuex";

import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    city: {
      historic: [],
      current: {}
    }
  },
  mutations: {
    setCityData(state, historicData, currentData) {
      state.city = {
        historic: historicData,
        current: currentData
      };
    }
  },
  actions: {
    setCityData() {
      // console.log("uau");
      axios
        .get(`${process.env.VUE_APP_API_URL}rio_city`, {
          headers: {
            "Access-Control-Allow-Origin": "*"
          }
        })
        .then(res => res)
        .catch(err => err);
    }
  },
  modules: {},
  getters: {}
});
