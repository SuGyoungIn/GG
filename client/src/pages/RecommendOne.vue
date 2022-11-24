<template>
  <div class="recommend1 gradient-custom">
    <div class="d-flex justify-content-between">
      <h2>랜덤으로 추천받기</h2>
      <div>
      <b-button @click="suffle">랜덤 돌리기</b-button>
      <b-dropdown :text="cnt + '개'">
        <b-dropdown-item @click="changeCnt(24)">24개 보기</b-dropdown-item>
        <b-dropdown-item @click="changeCnt(48)">48개 보기</b-dropdown-item>
        <b-dropdown-item @click="changeCnt(96)">96개 보기</b-dropdown-item>
        <b-dropdown-item @click="changeCnt(192)">192개 보기</b-dropdown-item>
        <b-dropdown-item @click="changeCnt(384)">384개 보기</b-dropdown-item>
      </b-dropdown>

      </div>
    </div>
    <div class="contain">
      <PosterCard
        v-for="(movie, idx) in on_view_movies"
        :key="idx"
        :movie="movie"
      />
    </div>
  </div>
</template>
<script>
import PosterCard from "../components/PosterCard.vue";

export default {
  props: {},
  components: {
    PosterCard,
  },
  created() {
    this.getMovies();
  },
  computed: {},
  data() {
    return {
      movies: [],
      on_view_movies: [],
      cnt: 24,
    };
  },
  methods: {
    getMovies() {
      this.$store.dispatch("getMovies");
      this.movies = this.$store.state.movies;
      this.suffle();
    },
    suffle() {
      this.movies.sort(() => Math.random() - 0.5);
      this.on_view_movies = this.movies.slice(0, this.cnt);
    },
    changeCnt(c) {
      this.cnt = c;
      this.on_view_movies = this.movies.slice(0, this.cnt);
    },
  },
};
</script>
<style scoped>
.recommend1 {
  padding: 2rem 10%;
  color:#fff;
}

.contain {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
}
</style>
