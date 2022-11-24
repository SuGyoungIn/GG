<template>
  
  <div class="recommend1 gradient-custom">
    
    <div><button @click="suffle">suffle</button></div>
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
  },
  data(){
    return{
      movies: [],
    }
  },
  methods: {
    getMovies(){
      this.$store.dispatch('getMovies')
      this.movies = this.$store.state.movies
      this.suffle()
    },
    suffle(){
      this.movies.sort(()=>Math.random()-0.5)
    }
  },
  
}
</script>
<style scoped>
.recommend1 {
  padding:0 10%;
}
.container{
  display: grid;
  grid-template-columns: repeat(6, 1fr);
}
</style>
