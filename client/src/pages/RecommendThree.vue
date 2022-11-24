<template>
  <div class="recommend3 gradient-custom">
    <div class="contain">
      <PosterCard
        v-for="(movie, idx) in rec_movies"
        :key="idx"
        :movie="movie"
      />
    </div>

    <h1>내가 좋아한 장르 지표</h1>
    <div class="chart-bg">
      <BarChart :genredata1="genredata1" />
    </div>

    <h1>내가 평가하는 장르 지표</h1>
    <div class="chart-bg">
      <BarChart2 :genredata2="genredata2" />
    </div>
  </div>
</template>
<script>
import PosterCard from "../components/PosterCard.vue";
import BarChart from "../components/BarChart.vue";
import BarChart2 from "../components/BarChart2.vue";
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
      NtoG: {
        12: 0,
        14: 1,
        16: 2,
        18: 3,
        27: 4,
        28: 5,
        35: 6,
        36: 7,
        37: 8,
        53: 9,
        80: 10,
        99: 11,
        878: 12,
        9648: 13,
        10402: 14,
        10749: 15,
        10751: 16,
        10752: 17,
        10770: 18,
      },
      rec_movies: [],
      genredata1: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

      genredata2: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      genredata2_sub1: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      genredata2_sub2: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

    };
  },
  methods: {
    async getMovies() {
      this.$store.dispatch("getGenres");
      this.genres = this.$store.state.genres;
      console.log(this.genres);

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
          })
          .catch((err) => {
            this.isLoading = false;
            console.log(err);
          });

        axios({
          method: "get",
          url: `${API_URL}/username/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`,
          },
        })
          .then((res) => {
            for (let idx1 in res.data.like_movies) {
              for (let idx2 in res.data.like_movies[idx1].genre_ids) {
                this.genredata1[this.NtoG[res.data.like_movies[idx1].genre_ids[idx2]]]++;
              }
            }
            for (let idx1 in res.data.user_comments) {
              for (let idx2 in res.data.user_comments[idx1].movie.genre_ids) {
                this.genredata2_sub1[this.NtoG[res.data.user_comments[idx1].movie.genre_ids[idx2]]]++;
                this.genredata2_sub2[this.NtoG[res.data.user_comments[idx1].movie.genre_ids[idx2]]]+=res.data.user_comments[idx1].stars;
              }
              for (let idx in this.genredata2){
                if (!this.genredata2_sub1[idx]) continue;
                this.genredata2[idx]=this.genredata2_sub2[idx]/this.genredata2_sub1[idx]
              }
            }
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
  padding: 0 10%;
}
.contain {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
}
.chart-bg {
  background-color: #fff;
}
</style>
