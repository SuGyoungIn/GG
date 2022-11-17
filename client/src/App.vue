<template>
  <div id="app" class="">
    <div class="bg-site">
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
            <router-link class="mx-2" to="/login">로그인</router-link>
            <router-link class="mx-2" to="/signup">회원가입</router-link>
            <router-link class="mx-2" to="/mypage/:user_id">마이페이지</router-link>
            <span class="mx-2" v-b-modal.searchModal> <img src="/img/search.png" alt="검색"> </span>
            <!-- Avatar -->
          </div>
          <!-- Right elements -->
        </div>
        <!-- Container wrapper -->
      </nav>



      <router-view />
    </div>
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
  data() {
    return {
      genres: [
        "모험",
        "판타지",
        "애니메이션",
        "드라마",
        "공포",
        "액션",
        "코미디",
        "역사",
        "서부",
        "스릴러",
        "범죄",
        "다큐멘터리",
        "SF",
        "미스터리",
        "음악",
        "로맨스",
        "가족",
        "전쟁",
        "TV 영화",
      ],
      selectedGenres: [],
    };
  },
  methods: {
    addGenre(genre) {
      if (!this.selectedGenres.includes(genre)) {
        this.selectedGenres.push(genre);
      }
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
