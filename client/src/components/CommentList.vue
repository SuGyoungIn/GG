<template>
  <div id="commentlist">
    <div>
      <form>
        <b-input-group :prepend="userName" class="mt-3">
          <b-form-input></b-form-input>
          <b-input-group-append>
            <b-form-rating inline v-model="rating"></b-form-rating>
            <b-button class="sub-btn">등록</b-button>
          </b-input-group-append>
        </b-input-group>
      </form>
    </div>

    <div class="comments">
      <ul class="list-group list-group-light">
        <li
          class="list-group-item d-flex justify-content-between align-items-center"
        >
          <div class="d-flex align-items-center">
            <img
              src="https://mdbootstrap.com/img/new/avatars/8.jpg"
              alt=""
              style="width: 45px; height: 45px"
              class="rounded-circle"
            />
            <div class="ml-3">
              <p class="fw-bold mb-1">John Doe</p>
              <p class="text-muted mb-0">john.doe@gmail.com</p>
            </div>
          </div>
          <span class="badge rounded-pill badge-success">Active</span>
        </li>
      </ul>
    </div>
  </div>
</template>
<script>
export default {
  created() {
    this.getUserName();
    this.getComments(this.movieId)
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    },
  },
  props: [],
  data() {
    return {
      userName: "",
      rating: 0,
      comments:[],
      isLoading: true,
    };
  },
  methods: {
    getUserName() {
      if (this.isLogin) {
        this.userName = this.$store.state.userData.username;
      } else {
        this.userName = "익명의 어피치";
      }
    },
    // getComments(){
    //   const API_URL = "http://127.0.0.1:8000";
    //   this.isLoading = true;
    // }
  },
};
</script>

<style scoped>
#commentlist {
  margin: 3vh 10%;
}
.sub-btn{
  background-color: #FFADAD;
}
</style>
