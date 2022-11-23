<template>
  <div class="poster-card" @click="moveToDetail(movie.id)">
    <img class="poster" :src="posterUrl + movie.poster_path" img-alt="Image">
  </div>
</template>
<script>
export default {
  data() {
    return {
      posterUrl: "https://image.tmdb.org/t/p/w500/",
    };
  },
  created() {

  },
  props: ["movie",],
  methods: {
    moveToDetail(movieId){
      this.$router.push({name:'detail', params: {movie_id: movieId}})
    }
  },
};
</script>
<style scoped>
.poster-card{
  cursor: pointer;
}

.poster{
  margin: 1vh;
  box-sizing: border-box;
  width: 12vw;
  height: 18vw;
}

.poster:hover {
  border: 5px solid #FFADAD;
}
</style>
