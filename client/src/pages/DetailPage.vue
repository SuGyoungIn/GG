<template>
  <div class="detail-page">
    <div>
      <img
        :src="imgBaseUrl + movieDetailData?.backdrop_path"
        alt="backdropImg"
      />
      <h2>{{ movieDetailData?.title }}</h2>
      <p>{{ movieDetailData?.homepage }}</p>
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
        <b-form-rating v-model="value" readonly></b-form-rating>
        {{ movieDetailData?.vote_average }} /
        {{ movieDetailData?.vote_count }}명
      </p>
    </div>

    <div>
      <form>
        <b-input-group :prepend="userName" class="mt-3">
          <b-form-input></b-form-input>
          <b-input-group-append>
            <b-form-rating v-model="value"></b-form-rating>
            <b-button variant="info">등록</b-button>
          </b-input-group-append>
        </b-input-group>
      </form>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  created() {
    this.getDetailMovieData(this.movieId);
  },
  data() {
    return {
      movieId: this.$route.params.movie_id,
      movieDetailData: {},
      imgBaseUrl: "",
      userName:"testName",
      value:0,
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
        console.log(this.movieDetailData);
      } catch (error) {
        console.log(error);
      }
    },
  },
  computed: {},
};
</script>
<style scoped></style>
