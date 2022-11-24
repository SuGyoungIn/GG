<template>
  <div id="carousel">
    <div class="contain">
      <b-row>
        <b-col cols="12">
          <div
            id="myCarousel"
            class="carousel slide"
            data-ride="carousel"
            data-interval="0"
          >
            <ol class="carousel-indicators">
              <li
                data-target="#myCarousel"
                data-slide-to="0"
                class="active"
              ></li>
              <li data-target="#myCarousel" data-slide-to="1"></li>
              <li data-target="#myCarousel" data-slide-to="2"></li>
            </ol>

            <div class="carousel-inner">
              <div class="carousel-item active">
                <b-row v-for="key in 3" :key="key">
                  <b-col cols="3" v-for="key in 4" :key="key">
                    <div class="thumb-wrapper">
                      <div class="img-box">
                        <img
                          src="https://picsum.photos/600/600/?image=25"
                          alt=""
                        />
                      </div>
                    </div>
                  </b-col>
                </b-row>
              </div>
            </div>
            <a
              class="carousel-control-prev"
              href="#myCarousel"
              data-slide="prev"
            >
              <BIconArrowLeft />
            </a>
            <a
                class="carousel-control-next"
                href="#myCarousel"
                data-slide="next"
              >
                <BIconArrowRight />
              </a>
          </div>
        </b-col>
      </b-row>
    </div>
  </div>
</template>
<script>
export default {
  created() {},
  props: ["movieId"],
  data() {
    return {};
  },
  methods: {},
};
</script>
<style scoped>
.carousel {
  margin: 50px auto;
  padding: 0 70px;
}
.carousel .carousel-item {
  min-height: 330px;
  text-align: center;
  overflow: hidden;
}
.carousel .carousel-item .img-box {
  height: 300px;
  width: 100%;
  position: relative;
}
.carousel .carousel-item img {
  max-width: 100%;
  max-height: 100%;
  display: inline-block;
  position: absolute;
  bottom: 0;
  margin: 0 auto;
  left: 0;
  right: 0;
}

.carousel .thumb-wrapper {
  text-align: center;
}

.carousel-control-prev,
.carousel-control-next {
  height: 100px;
  width: 40px;
  background: none;
  margin: auto 0;
  background: rgba(0, 0, 0, 0.2);
}
.carousel-control-prev svg,
.carousel-control-next svg {
  font-size: 30px;
  position: absolute;
  top: 50%;
  display: inline-block;
  margin: -16px 0 0 0;
  z-index: 5;
  left: 0;
  right: 0;
  color: rgba(0, 0, 0, 0.8);
  text-shadow: none;
  font-weight: bold;
}
.carousel-control-prev svg {
  margin-left: -3px;
}
.carousel-control-next svg {
  margin-right: -3px;
}

.carousel .carousel-indicators {
  bottom: -50px;
}
.carousel-indicators li,
.carousel-indicators li.active {
  width: 10px;
  height: 10px;
  margin: 4px;
  border-radius: 50%;
  border-color: transparent;
  border: none;
}
.carousel-indicators li {
  background: rgba(0, 0, 0, 0.2);
}
.carousel-indicators li.active {
  background: rgba(0, 0, 0, 0.6);
}

</style>
