import axios from "axios";
import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";
import router from "../router";

Vue.use(Vuex);

const API_URL = "http://127.0.0.1:8000";
export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    token: null,
    movies: [],
    articles: [],
    userData: [],
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies;
    },
    SAVE_TOKEN(state, token) {
      state.token = token;
      router.push({ name: "home" });
      console.log("로그인됐삼");
    },
    USER_DATA(state, userdata) {
      state.userData = userdata;
    },
    LOG_OUT(state) {
      state.token = null;
      state.userData = [];
      window.location.reload();
    },
  },
  actions: {
    getMovies(context) {
      axios({
        method: "get",
        url: `${API_URL}/movies/`,
      })
        .then((res) => {
          context.commit("GET_MOVIES", res.data);
        })
        .catch((err) => console.log(err));
    },
    signUp(context, payload) {
      const username = payload.username;
      const password1 = payload.password1;
      const password2 = payload.password2;
      const email = payload.email;

      axios({
        method: "post",
        url: `${API_URL}/accounts/signup/`,
        data: {
          username,
          password1,
          password2,
          email,
        },
      })
        .then((res) => {
          context.commit("SAVE_TOKEN", res.data.key);
        })
        .catch((err) => {
          console.log(err);
          alert("회원가입을 실패하였습니다.");
        });
    },
    logIn(context, payload) {
      const username = payload.username;
      const password = payload.password;

      axios({
        method: "post",
        url: `${API_URL}/accounts/login/`,
        data: {
          username,
          password,
        },
      })
        .then((res) => {
          context.commit("SAVE_TOKEN", res.data.key);
        })
        .catch((err) => {
          console.log(err);
          alert("로그인을 실패하였습니다.");
        });
    },
    logOut(context) {
      context.commit("LOG_OUT");
    },
    pushUserData(context, userdata){
      context.commit("USER_DATA", userdata)
    }
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false;
    },
  },
});
