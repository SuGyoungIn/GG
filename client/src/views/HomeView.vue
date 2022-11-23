<template>
  <div class="home">
       
    <section class="vh-100">
   
      <h1>{{ userName }}님께 맞는 영화조각을 찾아보세요!</h1>

      <div @click="moveToRecommend(1)" @mouseover="addToRecommend(1)" @mouseleave="addToRecommend(0)">
        <img id="puz1" class="puzzle" src="/img/puzzle1.png" alt="추천1" />
      </div>
      <div @click="moveToRecommend(2)" @mouseover="addToRecommend(2)" @mouseleave="addToRecommend(0)">
        <img id="puz2" class="puzzle" src="/img/puzzle2.png" alt="추천1" />
      </div>
      <div @click="moveToRecommend(3)" @mouseover="addToRecommend(3)" @mouseleave="addToRecommend(0)">
        <img id="puz3" class="puzzle" src="/img/puzzle3.png" alt="추천1" />
      </div>
      <p class="recommend-name">{{ recommendName }}</p>
    </section>
  </div>
</template>

<script>
export default {
  created() {
    this.getUserName();
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    },
  },
  data() {
    return {
      userName: "",
      recommendName: "",
    };
  },
  methods: {
    moveToRecommend(num) {
      const moveTo = "recommend" + num.toString();
      this.$router.push({ name: moveTo });
    },
    getUserName() {
      if (this.isLogin) {
        this.userName = this.$store.state.userData.username;
      } else {
        this.userName = "익명의 어피치";
      }
    },
    addToRecommend(num){
      if(num === 1) {
        this.recommendName = "랜덤으로 보는 영화조각"
      } else if(num === 2){
        this.recommendName = "장르로 찾아보는 영화조각"
      } else if(num === 3) {
        this.recommendName = "알고리즘으로 찾아보는 영화조각"
      } else if(num === 0) {
        this.recommendName = ""
      }
    },
  },
};
</script>

<style scoped>
.home {
  position: relative;
}

h1 {
  color: #fff;
  font-weight: 800;
  text-align: center;
}

.puzzle {
  cursor: pointer;
  height: 200px;
}

.puzzle:hover {
  height: 230px;
  transition: all 0.3s ease-in-out;
}

.puzzle:hover .recommend-name {
  display: inline;
}

#puz1 {
  position: absolute;
  top: 550px;
  left: 300px;
  transform: rotateZ(30deg);
  animation: movePuzzle 1s ease-in-out infinite;
}

#puz2 {
  position: absolute;
  top: 550px;
  right: 800px;
  transform: rotateZ(120deg);
  animation: movePuzzle 2s ease-in-out infinite;
}

#puz3 {
  position: absolute;
  top: 550px;
  right: 300px;
  transform: rotateZ(60deg);
  animation: movePuzzle 1.5s ease-in-out infinite;
}

.recommend-name {
  position: absolute;
  top: 60%;
  left: 35%;
  text-align: center;
  color: #fff;
  font-size: 48px;
  font-weight: 500;
  text-shadow: 3px 3px 7px #fff;
}

@keyframes movePuzzle {
  0% {
    top: 240px;
  }
  50% {
    top: 260px;
  }
  100% {
    top: 240px;
  }
}

@keyframes moveRecommendName {
  0% {
    top: 60%;
  }
  50% {
    top: 53%;
  }
  100% {
    top: 59%;
  }
}
</style>
