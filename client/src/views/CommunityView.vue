<template>
  <div id="community-view">
    <h1>커뮤니티</h1>
    <div class="community-banner">
      <b-button @click="moveToFindUser">유저 찾으러 가기 ></b-button>
    </div>
    <ArticleList />
  </div>
</template>
<script>
import ArticleList from "../components/ArticleList.vue";

export default {
  name: "CommunityView",
  components: { ArticleList },
  created() {
    this.getCommunity();
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    },
  },
  methods: {
    getCommunity() {
      if (!this.isLogin) {
        alert("로그인이 필요한 서비스 입니다.");
        this.$router.push({ name: "login" });
      }
    },
    moveToFindUser(){
      this.$router.push({ name: ""})
    }
  },
};
</script>
<style scoped>

#community-view {
  padding: 2rem 10%;
  color: #fff;
}
.community-banner {
  width: 100%;
  height: 30vh;
  background-color: #e1e1e1;
}
</style>
