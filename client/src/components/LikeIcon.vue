<template>
  <div id="like">
    <div class="like" @click="likeToggle">
      <BIconHeart class="h3" variant="light" v-if="!isLike" />
      <BIconHeartFill class="h3" variant="danger" v-if="isLike" />
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  created() {
    this.getLike(this.movieId)
  },
  props:["movieId"],
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    },
  },
  data() {
    return {
      isLike: false,
      likeUsers: [],
      userId: null,
    };
  },
  methods: {
    likeToggle() {
      if (this.isLike) {
        this.isLike = false;
        this.postLike(this.movieId)
      } else 
        this.isLike = true
        this.postLike(this.movieId)
    },
    async getLike(id){
      const API_URL = `http://127.0.0.1:8000/movies/${id}/likes/`;
      const token = `Token ${this.$store.state.token}`
      try{
        const response = await axios.get(API_URL, {
          headers: {
            Authorization : token,
          }
        })
        this.likeUsers = response.data.like_users
        if(this.isLogin){
          this.userId = this.$store.state.userData.id
          this.likeUsers.forEach(element => {
            if(element.id === this.userId){
              this.isLike = true;
            }
          });
        }
      } catch (error) {
        console.log(error)
      }
    },
    async postLike(id){
      const API_URL = `http://127.0.0.1:8000/movies/${id}/likes/`;
      const token = `Token ${this.$store.state.token}`
      try{
        const response = await axios.post(API_URL, {},{
          headers: {
            Authorization : token,
          }
        })
        this.likeUsers = response.data.like_users
        console.log(response.data)
        if(this.isLogin){
          this.userId = this.$store.state.userData.id
          this.likeUsers.forEach(element => {
            if(element.id === this.userId){
              this.isLike = true;
            }
          });
        }
        console.log(this.likeUsers)
      } catch (error) {
        console.log(error)
      }
    }
  },
};
</script>
<style scoped>
#like{
  cursor: pointer;
}
</style>
