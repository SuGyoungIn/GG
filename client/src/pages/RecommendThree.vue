<template>
  <div class="recommend3 gradient-custom">
    <div class="contain">
      <PosterCard
        v-for="(movie, idx) in rec_movies"
        :key="idx"
        :movie="movie"
      />
    </div>

    <h2>내가 좋아하는 장르</h2>
    <div class="chart-bg">
      <BarChart class="chart-body" />
    </div>

    <h2>나의 장르별 평가</h2>
    <div class="chart-bg">
      <BarChart2 class="chart-body" />
    </div>
  </div>
</template>
<script>
import PosterCard from "../components/PosterCard.vue";
import BarChart from "../components/BarChart.vue";
import BarChart2 from "../components/BarChart.vue";
import axios from "axios";

export default {
  props: {},
  components: {
    PosterCard,
    BarChart,
    BarChart2,
  },
  created() {
    this.getMovies();
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    },
  },
  data() {
    return {
      movies: [],
      rec_movies: [],
    };
  },
  methods: {
    async getMovies() {
      if (this.isLogin) {
        const API_URL = "http://127.0.0.1:8000";
        this.isLoading = true;
        axios({
          method: "get",
          url: `${API_URL}/movies/get_sim_items/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`,
          },
        })
          .then((res) => {
            this.rec_movies = res.data;
            console.log(this.rec_movies);
          })
          .catch((err) => {
            this.isLoading = false;
            console.log(err);
          });
      } else {
        alert("로그인이 필요한 서비스 입니다.");
        this.$router.push({ name: "login" });
      }
    },
  },
};
</script>
<style scoped>
.recommend3 {
  color: #fff;
  padding: 0 10%;
}
.contain {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
}
.chart-bg {
  position: relative;
  width: 100%;
  background-color: rgba(255, 255, 255, 0.701);
}
</style>
