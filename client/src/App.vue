<template>
  <div id="app">
    <!-- Navbar -->
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
              >마이프로필</b-dropdown-item
            >
            <b-dropdown-item @click="logOut">로그아웃</b-dropdown-item>
          </b-nav-item-dropdown>

          <span class="mx-2" v-b-modal.searchModal>
            <img src="/img/search.png" alt="검색" />
          </span>
          <!-- Avatar -->
        </div>
        <!-- Right elements -->
      </div>
      <!-- Container wrapper -->
    </nav>
    <router-view />

    <b-modal id="searchModal" title="검색" hide-footer size="xl">
      <b-container fluid>
        <b-row class="my-1">
          <b-col sm="10">
            <b-form-input
              id="input-default"
              placeholder="원하는 영화를 검색해보세요"
            ></b-form-input>
          </b-col>
          <b-col sm="2">
            <b-button>검색</b-button>
          </b-col>
        </b-row>
      </b-container>
      <hr />
      <div>
        <b-button v-b-toggle.collapse-1>상세설정</b-button>
        <b-collapse id="collapse-1" class="mt-2">
          <b-card>
            <b-row>
              <b-col sm="9">
                <p class="card-text">장르</p>
                <div>
                  <b-button
                    v-for="(genre, idx) in genres"
                    :key="idx"
                    @click="addGenre(genre)"
                    >{{ genre }}</b-button
                  >
                </div>
              </b-col>
              <b-col sm="3">
                <p class="card-text">별점</p>
              </b-col>
            </b-row>
          </b-card>
        </b-collapse>
      </div>
      <div>
        <div>
          <span>검색결과</span>

          <span v-if="selectedGenres.length > 0"
            ><b-button v-for="(selected, idx) in selectedGenres" :key="idx">{{
              selected
            }}</b-button></span
          >
        </div>
        <b-container>
          <b-row>
            <b-col
              ><b-card
                img-src="https://picsum.photos/400/400/?image=41"
                img-alt="Image"
                overlay
              ></b-card
            ></b-col>
            <b-col
              ><b-card
                img-src="https://picsum.photos/400/400/?image=41"
                img-alt="Image"
                overlay
              ></b-card
            ></b-col>
            <b-col
              ><b-card
                img-src="https://picsum.photos/400/400/?image=41"
                img-alt="Image"
                overlay
              ></b-card
            ></b-col>
            <b-col
              ><b-card
                img-src="https://picsum.photos/400/400/?image=41"
                img-alt="Image"
                overlay
              ></b-card
            ></b-col>
            <b-col
              ><b-card
                img-src="https://picsum.photos/400/400/?image=41"
                img-alt="Image"
                overlay
              ></b-card
            ></b-col>
            <b-col
              ><b-card
                img-src="https://picsum.photos/400/400/?image=41"
                img-alt="Image"
                overlay
              ></b-card
            ></b-col>
          </b-row>
        </b-container>
      </div>
    </b-modal>
  </div>
</template>

<script>
export default {
  created() {
    this.userData(),
    this.getUserData()
  },

  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    },

  },
  data() {
    return {
      genres: [],
      selectedGenres: [],
      user_id: 0,
      myPage: "myPage",
      username: "",
    };
  },
  methods: {
    addGenre(genre) {
      if (!this.selectedGenres.includes(genre)) {
        this.selectedGenres.push(genre);
      }
    },
    movePage(destination) {
      const userId = this.user_id;
      if (destination === "myPage") {
        this.$router.push({ name: "mypage", params: { user_id: userId } });
      }
    },
    logOut() {
      this.$store.dispatch("logOut");
    },
    userData() {
      if (this.isLogin) {
        this.$store.dispatch("getUserData");
      }
    },
    getUserData(){
      this.username = this.$store.state.userData.username
      this.user_id = this.$store.state.userData.user_pk
    }
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
</style>
