import Vue from "vue";
import Vuex from "vuex";
import axios from "axios"

Vue.use(Vuex);

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  state: {
    movies:[],
    articles:[],
  },
  mutations: {
    GET_MOVIES(state, movies){
      state.movies = movies
    }
  },
  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url:`${API_URL}/movies/`,
      })
      .then(res=>{
        console.log(res, context)
        context.commit('GET_MOVIES',res.data)
      })
      .catch(err=>{
        console.log(err)
      })
    }
  },
});
