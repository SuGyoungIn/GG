<template>
  <div class="poster-card" @click="moveToDetail(movie.fields.id)">
    <b-card :img-src="posterUrl + movie.fields.poster_path" img-alt="Image" overlay></b-card>
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
</style>
