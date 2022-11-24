<template>
  <div id="ArticlePage">
    <div class="article-body">
      <h2>{{ article.title }}</h2>
      <hr class="divider" />
      <div class="d-flex">
        <p class="mr-4">작성자 : {{ article.user.username }}</p>
        <p>작성일자 : {{ article.updated_at.slice(0, 10) }}</p>
      </div>
      <p>{{ article.content }}</p>
    </div>
    <div>
      <ArticleCommentList :articleId="article.id" :articleComments="article.comments"/>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import ArticleCommentList from "../components/ArticleCommentList.vue"
export default {
  name: "ArticlePage",
  created() {
    this.getArticle();
  },
  data() {
    return {
      id: this.$route.params.article_id,
      article: [],
    };
  },
  components: {ArticleCommentList},
  methods: {
    async getArticle() {
      const API_URL = `http://127.0.0.1:8000/community/articles/${this.id}/`;
      const token = `Token ${this.$store.state.token}`;
      try {
        const response = await axios.get(API_URL, {
          headers: {
            Authorization: token,
          },
        });
        this.article = response.data;
        console.log(this.article);
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>
<style scoped>
#ArticlePage {
  padding: 2rem 10%;
  color: #fff;
}

.divider {
  border-top: 1px solid #fff;
}
</style>
