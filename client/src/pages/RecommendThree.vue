<template>
  <div class="recommend3 gradient-custom">
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
    isLogin(){
      return this.$store.getters.isLogin
    }
  },
  data(){
    return{
      movies: [],
    }
  },
  methods: {
     getMovies(){
      if(this.isLogin){
        this.$store.dispatch('getMovies')
        this.movies = this.$store.state.movies
      } else {
        alert("로그인이 필요한 서비스 입니다.")
        this.$router.push({name: 'login'})
      }
    },
  },
  
}
</script>
<style scoped>
.recommend3 {
  padding:0 10%;
}
.container{
  display: grid;
  grid-template-columns: repeat(6, 1fr);
}
</style>
