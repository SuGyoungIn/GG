<template>
  <div class="detail-page">
    <div>
      <div class="container">
        <img
          :src="imgBaseUrl + movieDetailData?.backdrop_path"
          alt="backdropImg"
          class="backdropImg"
        />
        <h2 class="title">{{ movieDetailData?.title }}</h2>
        <span><BIconStarFill variant="warning"></BIconStarFill></span>
      </div>
      <span
        >장르 :
        <span v-for="genre in movieDetailData.genres" :key="genre.id"
          >{{ genre.name }}
        </span></span
      >
      <p>{{ movieDetailData?.overview }}</p>
      <img :src="imgBaseUrl + movieDetailData?.poster_path" alt="posterImg" />
      <p>{{ movieDetailData?.release_date }}</p>
      <p>{{ movieDetailData?.runtime }}분</p>
      <p>
        <b-form-rating v-model="value1" readonly></b-form-rating>
        {{ movieDetailData?.vote_average }} /
        {{ movieDetailData?.vote_count }}명
      </p>
      <div class="d-flex" v-if="profile5">
        <div v-for="(credit, key) in movieCredits5" :key="key">
          <img
            class="profile-img"
            :src="imgBaseUrl + credit.profile_path"
            alt="profile"
          />
          <p>
            {{ credit.name }}
          </p>
        </div>

        <b-button @click="profileMore(true)">더보기</b-button>
      </div>

      <div class="d-flex" v-if="profile10">
        <div v-for="(credit, key) in movieCredits10" :key="key">
          <img
            class="profile-img"
            :src="imgBaseUrl + credit.profile_path"
            alt="profile"
          />
          <p>
            {{ credit.name }}
          </p>
        </div>

        <b-button @click="profileMore(false)">접기</b-button>
      </div>
    </div>

    <CommentList />
  </div>
</template>
<script>
import axios from "axios";
import CommentList from "../components/CommentList.vue";

export default {
  created() {
    this.getDetailMovieData(this.movieId);
    this.getMovieCredits(this.movieId);
  },
  components: {
    CommentList,
  },
  data() {
    return {
      movieId: this.$route.params.movie_id,
      movieDetailData: {},
      movieCredits5: [],
      movieCredits10: [],
      imgBaseUrl: "",
      value1: 0,

      getSimilarMovies: {},
      getWatchProviders: {},
      profile5: true,
      profile10: false,
    };
  },
  methods: {
    async getDetailMovieData(id) {
      const API_KEY = process.env.VUE_APP_API_KEY;
      const API_URL = process.env.VUE_APP_API_URL + id.toString();
      this.imgBaseUrl = process.env.VUE_APP_API_IMG_URL;
      try {
        const response = await axios.get(API_URL, {
          params: {
            api_key: API_KEY,
            language: "ko-KR",
          },
        });
        this.movieDetailData = response.data;
        this.value1 = this.movieDetailData?.vote_average / 2;
      } catch (error) {
        console.log(error);
      }
    },
    async getMovieCredits(id) {
      const API_KEY = process.env.VUE_APP_API_KEY;
      const API_URL = process.env.VUE_APP_API_URL + id.toString() + "/credits";

      try {
        const response = await axios.get(API_URL, {
          params: {
            api_key: API_KEY,
            language: "ko-KR",
          },
        });
        const fullCredits = response.data.cast;
        this.movieCredits5 = fullCredits.slice(0, 5);
        this.movieCredits10 = fullCredits.slice(0, 10);
      } catch (error) {
        console.log(error);
      }
    },

    // async getSimilarMovies(id) {
    //   const API_KEY = process.env.VUE_APP_API_KEY;
    //   const API_URL = process.env.VUE_APP_API_URL + id.toString() + "/similar";

    //   try {
    //     const response = await axios.get(API_URL, {
    //       params: {
    //         api_key: API_KEY,
    //         language: "ko-KR",
    //       },
    //     });
    //     this.movieCredits = response.data.cast;
    //     console.log(this.movieCredits);
    //   } catch (error) {
    //     console.log(error);
    //   }
    // },
    // async getWatchProviders(id) {},
    profileMore(val) {
      if (val) {
        this.profile5 = false;
        this.profile10 = true;
      } else {
        this.profile5 = true;
        this.profile10 = false;
      }
    },
  },
  computed: {},
};
</script>
<style scoped>
.container {
  margin: 0;
  padding: 0;
  position: relative;
}

.title {
  font-size: 2.5rem;
  color: #ddd;
  position: absolute;
  bottom: 20%;
  left: 15%;
  text-shadow: 2px 2px 10px rgb(27, 27, 27);
}

.profile-img {
  width: 5vw;
}
.backdropImg {
  width: calc(100vw - 20px);
}
.backdropImg::after {
  content: "";
  background-color: rgba(0, 0, 0, 0.247);
}
.back-img {
}
</style>
