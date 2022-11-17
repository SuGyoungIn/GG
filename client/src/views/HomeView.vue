<template>
  <div class="home">
    <section class="vh-100 gradient-custom">
      <h1>{{ userName }}께 맞는 영화조각을 찾아보세요!</h1>

      <div>
        <img id="puz1" class="puzzle" src="/img/puzzle.png" alt="추천1" />
      </div>
      <div>
        <img id="puz2" class="puzzle" src="/img/puzzle 2.png" alt="추천1" />
      </div>
      <div>
        <img id="puz3" class="puzzle" src="/img/puzzle 3.png" alt="추천1" />
      </div>
    </section>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userName: "susu",
    };
  },
  methods: {},
};
</script>

<style scoped>
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

.puzzle{
  position: absolute;
  width:200px;
}

.puzzle:hover {
  box-shadow: 10px 5px 5px yellow;
}

#puz1 {
  top: 250px;
  left: 300px;
  transform: rotateZ(30deg);
  animation: movePuzzle 1.5s ease-in-out infinite;
}

#puz2 {
  top: 250px;
  right: 300px;
  transform: rotateZ(60deg);
  animation: movePuzzle 1.5s ease-in-out infinite;
}

#puz3 {
  top: 350px;
  right: 800px;
  transform: rotateZ(120deg);
  animation: movePuzzle 1.5s ease-in-out infinite;
}

@keyframes movePuzzle{
  0%{
    top: 240px;
  }
  50%{
    top:260px;
  }
  100%{
    top:240px;
  }
}
</style>
