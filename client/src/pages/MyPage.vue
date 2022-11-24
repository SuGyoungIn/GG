<template>
  <div class="my-page">
    <h1>my-page</h1>

    <div class="d-grid">
      <b-row>
        <b-col cols="2">
          <div>
            <p class="mypage-link">마이프로필</p>
          </div>
        </b-col>

        <b-col cols="10">
          <div>
            <MyProfile />
          </div>
        </b-col>
      </b-row>
    </div>
  </div>
</template>

<script>
import MyProfile from "../components/MyProfile.vue";

export default {
  created() {},
  components: {
    MyProfile,
  },
  data() {
    return {};
  },
};
</script>

<style scoped>
.col {
  padding: 0;
}
</style>
