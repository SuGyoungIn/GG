<template>
  <div id="like">
    <div class="like" @click="likeToggle">
      <BIconHeart class="h3" variant="light" v-if="!isLike" />
      <BIconHeartFill class="h3" variant="danger" v-if="isLike" />
    </div>
  </div>
</template>
<script>
export default {
  created() {},
  props:["movieId"],
  data() {
    return {
      isLike: false,
    };
  },
  methods: {
    likeToggle() {
      if (this.isLike) {
        this.isLike = false;
      } else this.isLike = true;
    },
    async getLike(){}
  },
};
</script>
<style scoped>
#like{
  cursor: pointer;
}
</style>
