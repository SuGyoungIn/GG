<template>
  <div id="commentlist">
    <div>
      <form @submit.prevent="postComment(movieId)">
        <b-input-group :prepend="userName" class="mt-3">
          <b-form-input v-model="content" :placeholder="preHolder"></b-form-input>
          <b-input-group-append>
            <b-form-rating inline v-model="stars"></b-form-rating>
            <b-button class="sub-btn" type="submit">등록</b-button>
          </b-input-group-append>
        </b-input-group>
      </form>
    </div>

    <div class="comments">
      <ul class="list-group list-group-light">
        <li
          class="list-group-item d-flex justify-content-between align-items-center"
          v-for="(comment, key) in comments"
          :key="key"
        >
          <div class="d-flex align-items-center">
            <b-avatar></b-avatar>
            <div class="ml-3">
              <p class="fw-bold mb-1">{{ comment.user.username }}</p>
              <p class="text-muted mb-0">{{ comment.content }}</p>
            </div>
          </div>
          <span>
            <BIconStarFill
              variant="warning"
              v-for="key in parseInt(comment.stars)"
              :key="key"
            ></BIconStarFill>
          </span>
        </li>
      </ul>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  created() {
    this.getUserName();
    this.getComments(this.movieId);
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    },
  },
  props: ["movieId"],
  data() {
    return {
      userName: "",
      stars: 0,
      content: "",
      comments: [],
      isLoading: true,
      preHolder: ""
    };
  },
  methods: {
    getUserName() {
      if (this.isLogin) {
        this.userName = this.$store.state.userData.username;
        this.preHolder = "댓글을 입력하세요"
      } else {
        this.userName = "익명의 어피치";
        this.preHolder = "로그인 이후 이용이 가능합니다."
      }
    },
    getComments(id) {
      const API_URL = "http://127.0.0.1:8000";
      this.isLoading = true;
      axios({
        method: "get",
        url: `${API_URL}/movies/${id}/comments/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          this.comments = res?.data;
          this.isLoading = false;
        })
        .catch((err) => {
          this.isLoading = false;
          console.log(err);
        });
    },
    postComment(id){
      const API_URL = "http://127.0.0.1:8000";
      const content = this.content
      const stars = Number(this.stars)
      axios({
        method: "post",
        url: `${API_URL}/movies/${id}/comments/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
        data: {content, stars}
      })
      .then(res => {
        this.comments = res?.data;
        this.getComments(id);
      })
      .catch((err =>
        console.log(err)
      ))
    }
  },
};
</script>

<style scoped>
#commentlist {
  margin: 3vh 10%;
}
.sub-btn {
  background-color: #ffadad;
}
</style>
