<template>
  <div id="watch-provider">
    <span>
      <img class="logo mr-2" :src="imgBaseUrl + watch.logo_path" alt="watch-provider-logo" v-for="watch,key in watchProviders" :key="key">
    </span>
  </div>
</template>
<script>
import axios from "axios";

export default {
  created() {
    this.getWatchProviders(this.movieId)
  },
  props: ["movieId"],
  data() {
    return {
      imgBaseUrl:"",
      watchProviders: [],
    };
  },
  methods: { 
    async getWatchProviders(id) {
      const API_KEY = process.env.VUE_APP_API_KEY;
      const API_URL = process.env.VUE_APP_API_URL + id.toString() + "/watch/providers";
      this.imgBaseUrl = process.env.VUE_APP_API_IMG_URL;
      try {
        const response = await axios.get(API_URL, {
          params: {
            api_key: API_KEY,
            language: "ko-KR",
          },
        });
        this.watchProviders = response.data.results.KR.flatrate;
      } catch (error) {
        console.log(error);
      }
    } 
    },
};
</script>
<style scoped>
.logo{
  width: 3vw;
  border-radius: .5vw;
}
</style>
