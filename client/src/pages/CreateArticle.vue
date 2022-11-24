<template>
  <div id="createArticle">
    <h1>글쓰기</h1>
    <form class="mt-5" @submit.prevent="postArticle">
      <b-form-input id="title" class="mb-4" placeholder="제목을 입력하세요" v-model="title"></b-form-input>
      <b-form-textarea
        id="textarea-rows"
        placeholder="내용을 입력하세요."
        rows="8"
        v-model="content"
      ></b-form-textarea>
      <b-btn class="mt-4" type="submit">작성완료</b-btn>
    </form>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      title:"",
      content: "",
    }
  },
  methods: {
    async postArticle(){
      const title = this.title
      const content = this.content
      const user = this.$store.state.userData.username
      const API_URL = "http://127.0.0.1:8000/community/articles/";
      const token = `Token ${this.$store.state.token}`
      try {
        await axios.post(API_URL,{
          title: title,
          content: content,
          user: user,
        },{
          headers: {
            Authorization : token,
          }
        })
        this.$router.push({ name: "community"})
      } catch (error) {
        console.log(error)
      }
    }
  }
};
</script>
<style scoped>
#createArticle {
  height: calc(100vh - 72px);
  padding: 2rem 10%;
  color: #fff;
}
</style>
