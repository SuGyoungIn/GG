<template>
  <div id="my-profile">
    <b-avatar :text="username"></b-avatar>
    <p>{{ username }}</p>
    <p>{{ userData.email }}</p>
    <div>
      <h3>좋아요한 영화목록</h3>
        <p v-if="userData.like_movies.length === 0">
          좋아요 누른 영화가 없습니다.
        </p>
        <PosterCard />
    </div>
  </div>
</template>
<script>
// import axios from "axios";
import PosterCard from "../components/PosterCard.vue"
export default {
  created() {
    this.getUserData()
  },
  components: {
    PosterCard
  },
  props: [],
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    },
  },
  data(){
    return {
      username: "",
      userData: {}
    }
  },
  methods: {
    getUserData(){
      if(this.isLogin){
        this.userData = this.$store.state.userData
        console.log(this.userData)
        this.username = this.userData.username
      }
    }
  }
}
</script>
<style scoped>
#my-profile {
  background-color: #fff
}

.b-avatar {
  width: 12rem;
  height: 12rem;
  font-size: 3rem;
}

</style>