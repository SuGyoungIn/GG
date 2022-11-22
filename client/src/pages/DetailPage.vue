<template>
  <div id="detail-page">
    <div class="hero-container">
      <img
        :src="imgBaseUrl + movieDetailData?.backdrop_path"
        alt="backdropImg"
        class="hero-img"
      />
      <span class="title-container">
        <h2 class="title">{{ movieDetailData?.title }}</h2>
        <span class="h3 rate-star">
          <BIconStarFill
            variant="warning"
            v-for="key in intCnt"
            :key="key"
          ></BIconStarFill>
          <BIconStarHalf variant="warning" v-if="floatCnt"></BIconStarHalf>
          /
          {{ movieDetailData?.vote_count }}명
        </span>
        <h4 class="detail-text ml-3">{{ releaseDate }}</h4>
        <h5 class="detail-text ml-3">{{ movieDetailData?.runtime }}분</h5>
      </span>

      <p class="detail-text overview">
        {{ movieDetailData?.overview }}
      </p>
      <span class="detail-text genre"
        >장르 :
        <span v-for="genre in movieDetailData.genres" :key="genre.id"
          >{{ genre.name }}
        </span>
      </span>
      <p class="credit detail-text">등장인물</p>
      <div class="d-flex align-items-start profiles" v-if="profile5">
        <div
          class="profile-container"
          v-for="(credit, key) in movieCredits5"
          :key="key"
        >
          <img
            class="profile-img"
            :src="imgBaseUrl + credit.profile_path"
            alt="profile"
          />
          <p class="profile-name detail-text">
            {{ credit.name }}
          </p>
        </div>

        <b-button class="profile-btn mt-5" @click="profileMore(true)"
          >더보기</b-button
        >
      </div>

      <div class="d-flex align-items-start profiles" v-if="profile10">
        <div
          class="profile-container"
          v-for="(credit, key) in movieCredits10"
          :key="key"
        >
          <img
            class="profile-img"
            :src="imgBaseUrl + credit.profile_path"
            alt="profile"
          />
          <p class="profile-name detail-text">
            {{ credit.name }}
          </p>
        </div>
        <b-button class="profile-btn mt-5" @click="profileMore(false)"
          >접기</b-button
        >
      </div>
        <LikeIcon class="like"/>
      
    </div>

    <CommentList />
  </div>
</template>
<script>
import axios from "axios";
import CommentList from "../components/CommentList.vue";
import LikeIcon from "../components/LikeIcon.vue";

export default {
  created() {
    this.getDetailMovieData(this.movieId);
    this.getMovieCredits(this.movieId);
  },
  components: {
    CommentList,
    LikeIcon
  },
  data() {
    return {
      movieId: this.$route.params.movie_id,
      releaseDate: "",
      movieDetailData: {},
      movieCredits5: [],
      movieCredits10: [],
      imgBaseUrl: "",
      intCnt: 0,
      floatCnt: false,
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
        this.intCnt = parseInt(this.movieDetailData?.vote_average / 2);
        if (this.movieDetailData?.vote_average / 2 - this.intCnt >= 0.25) {
          this.floatCnt = true;
        }
        this.releaseDate = this.movieDetailData?.release_date.split("-")[0];
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
#detail-page {
  background: linear-gradient(
    to right,
    rgba(106, 17, 203, 1),
    rgba(37, 117, 252, 1)
  );
}

.hero-container {
  width: 100%;
  margin: 0;
  padding: 0;
  position: relative;
  background: linear-gradient(90deg, rgb(255, 255, 255), rgb(0, 0, 0) 50%);
}

.title-container {
  display: flex;
  align-items: end;
  position: absolute;
  top: 15%;
  left: 10%;
  text-shadow: 3px 3px 5px rgb(0, 0, 0);
}

.hero-img {
  width: 100%;
  opacity: 30%;
}

.title {
  font-size: 3.5vw;
  color: #ddd;
}
.rate-star {
  margin-left: 1vw;
  color: #ddd;
}

.detail-text {
  color: #eee;
  text-shadow: 2px 2px 3px rgb(0, 0, 0);
}

.overview {
  width: 80%;
  position: absolute;
  top: 30%;
  left: 10%;
}

.genre {
  position: absolute;
  top: 47%;
  left: 10%;
}

.credit {
  position: absolute;
  top: 55%;
  left: 10%;
}
.profiles {
  position: absolute;
  top: 60%;
  left: 10%;
}
.profile-container {
  width: 5vw;
  margin-right: 1vw;
}

.profile-img {
  width: 5vw;
}

.profile-btn {
  height: 4vh;
}

.profile-name {
  word-wrap: break-all;
}

.like{
  position: absolute;
  top: 88%;
  left: 10%;
  cursor: pointer;
}

</style>
