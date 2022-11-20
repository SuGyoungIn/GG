<template>
  <div class="home">
    <section class="vh-100 gradient-custom">
      <h1>{{ userName }}께 맞는 영화조각을 찾아보세요!</h1>

      <div @click="moveToRecommend(1)" @hover="addToRecommend(1)">
        <img id="puz1" class="puzzle" src="/img/puzzle1.png" alt="추천1" />
      </div>
      <div @click="moveToRecommend(2)" @hover="addToRecommend(2)">
        <img id="puz2" class="puzzle" src="/img/puzzle2.png" alt="추천1" />
      </div>
      <div @click="moveToRecommend(3)" @hover="addToRecommend(1)">
        <img id="puz3" class="puzzle" src="/img/puzzle3.png" alt="추천1" />
      </div>
      <p class="recommend-name">{{ recommendName }}</p>
    </section>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userName: "susu",
      recommendName: "test test",
    };
  },
  methods: { 
    moveToRecommend(num) {
      const moveTo = 'recommend' + num.toString()
      this.$router.push({name: moveTo})
    }, },}
</script>

<style scoped>

.home{
  position: relative;
}

.gradient-custom {
  padding: 10px 10%;
  overflow: hidden;
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
  transition: all 0.3s ease-in-out
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

#puz2{
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
  left: 45%;
  text-align: center;
  color: #fff;
  font-size: 48px;
  font-weight: 700;
  display:none;
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
    top: 53%
  }
  100% {
    top: 59%;
  }
}



</style>
