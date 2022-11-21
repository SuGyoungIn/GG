<template>
  <div class="recommend1">
    <div class="container">
        <PosterCard v-for="(movie,idx) in movies" :key="idx" :movie="movie" />
    </div>
  </div>
</template>
<script>
import PosterCard from "../components/PosterCard.vue" 

export default {
  props:{},
  components: {
    PosterCard
  },
  created(){
    this.getMovies()
  },
  computed:{
     movies(){
      return this.$store.state.movies
    },
  },
  data(){
    return{
    }
  },
  methods: {
    getMovies(){
      this.$store.dispatch('getMovies')
    }
  },
  
}
</script>
<style scoped>
.recommend1 {
  margin: 0 10%;
}
.container{
  display: grid;
  grid-template-columns: repeat(6, 1fr);
}
</style>
