<template>
  <div id="findUser">
    <h1>{{ username }}님과 비슷한 유저 찾기</h1>

    <div v-if="!isLoading" class="movie-container">
      <div v-if="likeMovieData.length < 5">
        <p>좋아요를 누른 영화 너무 적습니다.</p>
        <b-btn @click="moveToRecommend" >좋아요 누르러 가기</b-btn>
      </div>

      <div v-if="likeMovieData.length >= 5">
        <p>{{ username }}님과 비슷한 유저 목록</p>
        <div class="d-flex">
        <div v-for="user, key in simUser" :key="key" @click="moveToUserPage(user.id)" class="mr-3 user">
        <b-avatar :text="user.username.slice(0,3)" ></b-avatar>
        </div>
        </div>
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
      isLoading: true,
      username: "",
      simUser: [],
      likeMovieData: 0,
    };
  },

  methods: {
    async getSimUser() {
      if (this.isLogin) {
        const API_URL = "http://127.0.0.1:8000";
        this.username = this.$store.state.userData.username;
        this.likeMovieData = this.$store.state.userData.like_movies;
        this.isLoading = true;

        await axios({
          method: "get",
          url: `${API_URL}/movies/get_sim_user/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`,
          },
        })
          .then((res) => {
            this.isLoading = false;
            this.simUser = res.data;
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
    moveToRecommend(){
      this.$router.push({ name: "recommend2"})
    },
    moveToUserPage(id){
      console.log(id)
      this.$router.push({ name: "mypage", params: {user_id : id}})
    }

  },
};
</script>
<style scoped>
#findUser {
  padding: 2rem 10%;
  color: #fff;
  height: calc(100vh - 72px);
}

.user {
  cursor: pointer;
}
</style>
