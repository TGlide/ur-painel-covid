import Vue from "vue";
import Vuex from "vuex";

import axios from "axios";

import { dateCompare, dateToStr } from "../helpers/date";
import { getCharts } from "../helpers/chart";
import { getLocaleData } from "../helpers/locale";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    city: {
      historic: [],
      current: {}
    },

    state: {
      historic: [],
      current: {}
    },

    charts: {
      city: {},
      state: {}
    },

    locales: {
      state: [],
      city: [],
      aps: []
    },

    error: {
      status: false,
      message: undefined
    },
    loading: true
  },
  mutations: {
    setCityData(state, payload) {
      state.city = {
        ...payload
      };
    },

    setCharts(state, payload) {
      state.charts = {
        city: payload.city || {},
        state: payload.state || {}
      };
    },

    setStateData(state, payload) {
      state.state = {
        ...payload
      };
    },

    setLocaleData(state, payload) {
      state.locales = {
        state: payload.estado,
        city: payload.municipio,
        aps: payload.aps
      };
    },

    setError(state, payload) {
      state.error = {
        status: payload.status,
        message: payload.message
      };
    },

    setLoading(state, loadingStatus) {
      state.loading = loadingStatus;
    }
  },
  actions: {
    setAllData({ commit }) {
      const cityPromise = axios.get(
        `${process.env.VUE_APP_API_URL}api/rio_city`
      );
      const statePromise = axios.get(
        `${process.env.VUE_APP_API_URL}api/rio_state`
      );
      const neighborhoodPromise = axios.get(
        `${process.env.VUE_APP_API_URL}api/neighborhoods`
      );
      const citiesPromise = axios.get(
        `${process.env.VUE_APP_API_URL}api/cities`
      );
      const cityProjectionsPromise = axios.get(
        `${process.env.VUE_APP_PROJECTIONS_API_URL}projection/city`
      );
      const stateProjectionsPromise = axios.get(
        `${process.env.VUE_APP_PROJECTIONS_API_URL}projection/state`
      );

      Promise.all([
        cityPromise,
        statePromise,
        neighborhoodPromise,
        citiesPromise,
        cityProjectionsPromise,
        stateProjectionsPromise
      ])
        .then(values => {
          const [
            cityRes,
            stateRes,
            neighborhoodRes,
            citiesRes,
            cityProjectionsRes,
            stateProjectionsRes
          ] = values;

          let city = {
            historic: [],
            current: {},
            loading: false,
            error: false
          };
          city.historic = cityRes.data.sort(dateCompare).map(entry => {
            return { ...entry, date: dateToStr(entry.date) };
          });
          city.current = city.historic[city.historic.length - 1];
          commit("setCityData", { ...city });

          let state = {
            historic: [],
            current: {},
            loading: false,
            error: false
          };
          state.historic = stateRes.data.sort(dateCompare).map(entry => {
            return { ...entry, date: dateToStr(entry.date) };
          });
          state.current = state.historic[state.historic.length - 1];
          commit("setStateData", { ...state });

          const cityCharts = getCharts(
            city,
            cityProjectionsRes.data.data,
            "city"
          );
          const stateCharts = getCharts(
            state,
            stateProjectionsRes.data.data,
            "state"
          );
          commit("setCharts", { city: cityCharts, state: stateCharts });

          const localeData = getLocaleData(
            neighborhoodRes.data,
            citiesRes.data
          );
          commit("setLocaleData", localeData);
        })
        .catch(error => {
          commit("setError", { status: true, message: error });
        })
        .finally(() => {
          commit("setLoading", false);
        });
    }
  },
  getters: {
    city: state => state.city,
    charts: state => state.charts,
    state: state => state.state,
    locales: state => state.locales,
    error: state => state.error,
    loading: state => state.loading
  }
});
