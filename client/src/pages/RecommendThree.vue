<template>
  <div id="recommend3">
    <h2>{{ username }}님이 좋아할만한 영화</h2>
    <div class="contain mb-5">

      <PosterCard
        v-for="(movie, idx) in rec_movies"
        :key="idx"
        :movie="movie"
      />
    </div>
<<<<<<< HEAD

    <h1>내가 좋아한 장르 지표</h1>
    <div class="chart-bg">

      <BarChart v-if="!isLoading" :genredata1="genredata1" />

    </div>

    <h1>내가 평가하는 장르 지표</h1>
    <div class="chart-bg">

      <BarChart2 v-if="!isLoading" :genredata2="genredata2" />

=======
    <div class="mb-5">
      <h2>{{ username }}님이 좋아하는 장르 지표</h2>
      <div class="chart-bg">
        <BarChart :genredata1="genredata1" />
      </div>
    </div>

    <div class="mb-5">
      <h2>{{ username }}님이 평가한 장르 지표</h2>
      <div class="chart-bg">
        <BarChart2 :genredata2="genredata2" />
      </div>
>>>>>>> susu1
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

    this.getData();
    this.getRecMovies();

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
<<<<<<< HEAD
      genredata1: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

      genredata2: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      genredata2_sub1: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      genredata2_sub2: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      isLoading: true,
    };
  },
  methods: {
    async getData() {
=======
      genredata1: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      genredata2: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      genredata2_sub1: [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      ],
      genredata2_sub2: [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      ],
      username: "",
    };
  },
  methods: {
    async getMovies() {
>>>>>>> susu1
      if (this.isLogin) {
        const API_URL = "http://127.0.0.1:8000";
        this.username = this.$store.state.userData.username;
        this.isLoading = true;
<<<<<<< HEAD
        

        await axios({

=======

        axios({
>>>>>>> susu1
          method: "get",
          url: `${API_URL}/username/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`,
          },
        })
          .then((res) => {
            for (let idx1 in res.data.like_movies) {
              for (let idx2 in res.data.like_movies[idx1].genre_ids) {
                this.genredata1[
                  this.NtoG[res.data.like_movies[idx1].genre_ids[idx2]]
                ]++;
              }
            }
            for (let idx1 in res.data.user_comments) {
              for (let idx2 in res.data.user_comments[idx1].movie.genre_ids) {
                this.genredata2_sub1[
                  this.NtoG[res.data.user_comments[idx1].movie.genre_ids[idx2]]
                ]++;
                this.genredata2_sub2[
                  this.NtoG[res.data.user_comments[idx1].movie.genre_ids[idx2]]
                ] += res.data.user_comments[idx1].stars;
              }
              for (let idx in this.genredata2) {
                if (!this.genredata2_sub1[idx]) continue;
                this.genredata2[idx] =
                  this.genredata2_sub2[idx] / this.genredata2_sub1[idx];
              }
            }
<<<<<<< HEAD
            for (let idx1 in res.data.like_movies) {
              for (let idx2 in res.data.like_movies[idx1].genre_ids) {
                this.genredata1[this.NtoG[res.data.like_movies[idx1].genre_ids[idx2]]]++;
              }
            }
            console.log(this.genredata1,this.genredata2)
            this.isLoading = false

=======
            console.log(this.genredata1, this.genredata2);
>>>>>>> susu1
          })
          .catch((err) => {
            this.isLoading = false;
            console.log(err);
          });
<<<<<<< HEAD
      } else {
        alert("로그인이 필요한 서비스 입니다.");
        this.$router.push({ name: "login" });
      }
    },
    async getRecMovies() {

      if (this.isLogin) {
        const API_URL = "http://127.0.0.1:8000";
        this.isLoading = true;
        await axios({
=======
        axios({
>>>>>>> susu1
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
      } else {
        alert("로그인이 필요한 서비스 입니다.");
        this.$router.push({ name: "login" });
      }
    },
  },
};
</script>
<style scoped>
<<<<<<< HEAD
.recommend3 {
  color: #fff;
  padding: 0 10%;
=======
#recommend3 {
  color: #fff;
  padding: 2rem 10%;

>>>>>>> susu1
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
