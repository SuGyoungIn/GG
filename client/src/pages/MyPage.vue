<template>
  <div id="my-profile">
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
// import axios from "axios";
import PosterCard from "../components/PosterCard.vue";
export default {
  created() {
    this.getUserData();
  },
  components: {
    PosterCard,
  },
  props: [],
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    },
  },
  data() {
    return {
      username: "",
      userData: {},
      likeMovieData: [],
      commentMovieData: [],
      show: true,
    };
  },
  methods: {
    getUserData() {
      if (this.isLogin) {
        this.userData = this.$store.state.userData;
        this.username = this.userData.username;
        this.likeMovieData = this.userData.like_movies;
        this.commentMovieData = this.userData.user_comments;
        console.log(this.userData);
      }
    },
    showList(num) {
      if (num === 1) {
        this.show = true;
      } else if (num === 2) {
        this.show = false;
      }
    },
  },
};
</script>
<style scoped>
#my-profile {
  padding: 2rem 10%;
  background-color: #fff;
  color: #fff;
}

.b-avatar {
  width: 12rem;
  height: 12rem;
  font-size: 3rem;
}

h3 {
  cursor: pointer;
}

h3:hover {
  color: #ffadad;
}

.detail-text {
  font-size: 1.5rem;
}

.movie-container {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
}
</style>
