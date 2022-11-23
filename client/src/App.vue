<template>
  <div id="app">
    <div class="spinner" v-if="isLoading">
      <b-spinner
        variant="dark"
        style="width: 3rem; height: 3rem"
        label="Large Spinner"
      ></b-spinner>
    </div>
 <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light py-3">
      <!-- Container wrapper -->
      <div class="container-fluid">
        <!-- Collapsible wrapper -->
        <div class="" id="navbarSupportedContent">
          <!-- Navbar brand -->
          <router-link to="/"
            ><img src="/LOGO.png" alt="logo" style="width: 100px"
          /></router-link>
          <!-- Left links -->
        </div>

        <!-- Right elements -->
        <div class="d-flex align-items-center">
          <!-- Icon -->
          <router-link class="mx-2" to="/community">커뮤니티</router-link>
          <router-link class="mx-2" to="/login" v-if="!isLogin"
            >로그인</router-link
          >
          <router-link class="mx-2" to="/signup" v-if="!isLogin"
            >회원가입</router-link
          >
          <b-nav-item-dropdown :text="username" v-if="isLogin">
            <b-dropdown-item @click="movePage(myPage)"
              >마이페이지</b-dropdown-item
            >
            <b-dropdown-item @click="logOut">로그아웃</b-dropdown-item>
          </b-nav-item-dropdown>

          <span class="mx-2" v-b-modal.searchModal>
            <img src="/img/search.png" alt="검색" @click="getMovies"/>

          </span>
          <!-- Avatar -->
        </div>
        <!-- Right elements -->
      </div>
      <!-- Container wrapper -->
    </nav>
  </div>
    <!-- <div class="container" v-if="!isLoading">
      
    </div> -->
    <router-view class="gradient-custom"/>
      <SearchModal :movies="movies" :genres="genres"/>
  </div>
</template>

<script>
import axios from "axios";
import SearchModal from "./components/SearchModal.vue";

export default {
  created() {
    this.getUserData();
  },
  components: {
    SearchModal,

  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    },
  },
  data() {
    return {
      userId: null,
      myPage: "myPage",
      username: "",
      isLoading: false,
      movies:[],
      genres:[],
    };
  },
  methods: {
    addGenre(genre) {
      if (!this.selectedGenres.includes(genre)) {
        this.selectedGenres.push(genre);
      }
    },
    logOut() {
      this.$store.dispatch("logOut");
    },
    getUserData() {
      const API_URL = "http://127.0.0.1:8000";
      this.isLoading = true;
      axios({
        method: "get",
        url: `${API_URL}/username/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          this.$store.dispatch("pushUserData", res.data);
          this.username = res.data.username;
          this.userId = res.data.id;
          this.isLoading = false;
          console.log(this.isLoading);
        })
        .catch((err) => {
          this.isLoading = false;
          console.log(err);
        });
    },
    getMovies(){
      this.$store.dispatch('getMovies')
      this.movies = this.$store.state.movies
      this.$store.dispatch('getGenres')
      this.genres = this.$store.state.genres
    },
  },
};
</script>

<style>
* {
  font-family: "Nanum Gothic", sans-serif;
}
#app {
  position: relative;
}
ul {
  padding: 0;
}
li {
  list-style: none;
}

a {
  text-decoration: none;
  color: #333;
  font-weight: 400;
}
.navbar {
  padding: 0 10% !important;
  background-color: #212529;
}
.spinner {
  position: absolute;
  top: 50%;
  left: 45%;
  z-index: 4;
}
.gradient-custom {
  /* fallback for old browsers */
  background: #6a11cb;

  /* Chrome 10-25, Safari 5.1-6 */
  background: -webkit-linear-gradient(
    to right,
    rgba(106, 17, 203, 1),
    rgba(37, 117, 252, 1)
  );

  /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  background: linear-gradient(
    to right,
    rgba(106, 17, 203, 1),
    rgba(37, 117, 252, 1)
  );
}
</style>
