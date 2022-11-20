<template>
  <div id="ArticleList">
    <b-table hover :items="articles" :fields="fields" >
      <template #cell(인덱스)="data">
          {{ data.index + 1 }}
      </template>
      <template #cell(제목)="data">

        <p class="article" @click="moveTo(data.item.id)">{{ data.item.제목 }}</p>
      </template>
    </b-table>
  </div>
</template>
<script>

export default {
  name: "ArticleList",
  created(){
    this.getItems()
  },
  data(){
    return{
      articles:[],
      fields:["인덱스","제목", "작성자", "작성시간"],
    }
  },
  components:{

  },
  methods: {
    getItems(){
      const articlesData = this.$store.state.articles
      this.articles = articlesData
    },
    moveTo(id){
      this.$router.push({name:'article', params:{article_id:id}})
    }
  }
}
</script>
<style scoped>
  .article {
    cursor: pointer;
  }
</style>