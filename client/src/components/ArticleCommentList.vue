<template>
  <div id="commentlist">
    <div>
      <form @submit.prevent="postComment(articleId)">
        <b-input-group :prepend="userName" class="mt-3">
          <b-form-input
            v-model="content"
            :placeholder="preHolder"
          ></b-form-input>
          <b-input-group-append>
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
              <p class="fw-bold mb-1 user">{{ comment.user.username }}</p>
              <p class="text-muted mb-0">{{ comment.content }}</p>
            </div>
          </div>
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
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    },
  },
  props: ["articleComments","articleId"],
  data() {
    return {
      userName: "",
      content: "",
      comments: this.articleComments,
      isLoading: true,
      preHolder: "",
    };
  },
  methods: {
    getUserName() {
      if (this.isLogin) {
        this.userName = this.$store.state.userData.username;
        this.preHolder = "댓글을 입력하세요";
      } else {
        this.userName = "익명";
        this.preHolder = "로그인 이후 이용이 가능합니다.";
      }
    },
    postComment(id) {
      const API_URL = "http://127.0.0.1:8000";
      const content = this.content;
      axios({
        method: "post",
        url: `${API_URL}/community/articles/${id}/comments/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
        data: {content},
      })
        .then((res) => {
          this.comments = res?.data;
          window.location.reload();
        })
        .catch((err) => console.log(err));
    },
  },
};
</script>

<style scoped>
.user {
  color: #333;
}
</style>
