<template>
  <div id="find_user">
    <h1>{{ username }}님의 페이지</h1>
    <div class="d-flex justify-content-">
      <b-avatar :text="username"></b-avatar>

      <div class="ml-5 pt-4">
        <p class="detail-text">ID : {{ username }}</p>
        <p class="detail-text">EMAIL : {{ userData.email }}</p>
      </div>
    </div>
    <div class="d-flex my-4">
      <h3 class="mr-4" @click="showList(1)">좋아요 영화목록</h3>
      <h3 @click="showList(2)">댓글 영화목록</h3>
    </div>

    <div v-if="show" class="movie-container">
      <p v-if="likeMovieData.length === 0">좋아요를 누른 영화가 없습니다.</p>
      <div v-if="likeMovieData" class="movie-container">
        <PosterCard
          v-for="(movie, key) in likeMovieData"
          :movie="movie"
          :key="key"
        />
      </div>
    </div>

    <div v-if="!show">
      <p v-if="commentMovieData.length === 0">댓글을 쓴 영화가 없습니다.</p>
      <div v-if="commentMovieData" class="movie-container">
        <PosterCard
          v-for="(movie, key) in commentMovieData"
          :movie="movie.movie"
          :key="key"
        />
      </div>
    </div>
  </div>
</template>




<script>
import axios from "axios";
export default {
  created() {
    this.getSimUser();
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    },
  },
  data() {
    return {
      isLoading:true,
      username:'',
    }
  },

  methods: {
    async getSimUser() {
      if (this.isLogin) {
        const API_URL = "http://127.0.0.1:8000";
        this.username = this.$store.state.userData.username;
        this.isLoading = true;
        

        await axios({

          method: "get",
          url: `${API_URL}/movies/get_sim_user/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`,
          },
        })
          .then((res) => {
            console.log(res)
            this.isLoading = false

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
}
</script>
<style scoped>

</style>