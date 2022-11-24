<template>
  <div id="articleList">
    <b-table hover :items="articles" :fields="fields" dark head-variant="light">
      <template #cell(인덱스)="data">
        {{ data.index + 1 }}
      </template>

      <template #cell(제목)="data">
        <p class="article" @click="moveTo(data.item.id)">
          {{ data.item.title }}
        </p>
      </template>
      <template #cell(작성자)="data">
        <p class="article" @click="moveTo(data.item.id)">
          {{ data.item.user.username }}
        </p>
      </template>

      <template #cell(작성시간)="data">
        <p class="article" @click="moveTo(data.item.id)">
          {{ data.item.updated_at.slice(0,10) }}
        </p>
      </template>
    </b-table>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "ArticleList",
  created() {
    this.getArticles();
  },
  data() {
    return {
      articles: [],
      fields: ["인덱스", "제목", "작성자", "작성시간"],
      updated_at: ""
    };
  },
  components: {},
  methods: {
    async getArticles() {
      const API_URL = `http://127.0.0.1:8000/community/articles/`;
      const token = `Token ${this.$store.state.token}`;
      try {
        const response = await axios.get(API_URL, {
          headers: {
            Authorization: token,
          },
        });
        this.articles = response.data;
      } catch (error) {
        console.log(error);
      }
    },
    moveTo(id) {
      this.$router.push({ name: "article", params: { article_id: id } });
    },
  },
};
</script>
<style scoped>
#articleList {
  color: #fff;
}
.article {
  cursor: pointer;
}
</style>
