<template>
  <div id="poster-carousel">
    <div>
      <img class="similar" :src="imgBaseUrl + movie.poster_path" alt="similarMovie" v-for="movie, key in similarMovies" :key="key">
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  created() {
    this.getSimilarMovies(this.movieId)
  },
  props:['movieId'],
  data(){
    return{
      similarMovies: [],
      imgBaseUrl:""
    }
  },
  methods: {
    async getSimilarMovies(id) {
      const API_KEY = process.env.VUE_APP_API_KEY;
      const API_URL = process.env.VUE_APP_API_URL + id.toString() + "/similar";
      this.imgBaseUrl = process.env.VUE_APP_API_IMG_URL;
      try {
        const response = await axios.get(API_URL, {
          params: {
            api_key: API_KEY,
            language: "ko-KR",
          },
        });
        this.similarMovies = response.data.results.slice(0,7);

      } catch (error) {
        console.log(error);
      }
    },
  }
}
</script>
<style scoped>
.similar {
  width: 10vw;
  height: 15vw;
  margin-right: 1vw;
}
</style>