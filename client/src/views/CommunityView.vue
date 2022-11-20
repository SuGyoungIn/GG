<template>
  <div id="CommunityView">
    <h1>community</h1>
    <div class="community-banner">
      <b-button>유저 찾으러 가기 ></b-button>
    </div>
    <ArticleList/>
  </div>
</template>
<script>
import ArticleList from "../components/ArticleList.vue"
export default {
  name:"CommunityView",
  components:{ArticleList},
}
</script>
<style scoped>
.community-banner {
  width: 100%;
  height: 30vh;
  background-color: #e1e1e1;
}
</style>
