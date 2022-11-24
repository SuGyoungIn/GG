<template>
  <div id="my-profile">
    <b-avatar :text="username"></b-avatar>
    <p>{{ username }}</p>
    <p>{{ userData.email }}</p>
    <div class="d-flex">
      <h3 class="mr-4" @click="showList(1)">좋아요 영화목록</h3>

      <h3 @click="showList(2)">댓글 영화목록</h3>
    </div>

    <div v-if="show">
      <p v-if="likeMovieData.length === 0">
        좋아요를 누른 영화가 없습니다.
      </p>
      <div v-if="likeMovieData">
        <PosterCard
          v-for="(movie, key) in likeMovieData"
          :movie="movie"
          :key="key"
        />
      </div>
    </div>

    <div v-if="!show">
      <p v-if="commentMovieData.length === 0">
        댓글을 쓴 영화가 없습니다.
      </p>
      <div v-if="commentMovieData">
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
        console.log(this.userData)


      }
    },
    showList(num){
      if(num === 1){
        this.show = true
      } else if(num === 2) {
        this.show = false
      }
    }
  },
};
</script>
<style scoped>
#my-profile {
  background-color: #fff;
}

.b-avatar {
  width: 12rem;
  height: 12rem;
  font-size: 3rem;
}

h3 {
  cursor: pointer;
}
</style>
