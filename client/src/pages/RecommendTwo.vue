<template>
  <div id="recommend2">
    <div>
      <h2>
        {{ selectedGenre }}
      </h2>
      <b-dropdown text="장르 선택">
        <b-dropdown-item v-for="value ,genre ,key of sorted_movies" :key="key" @click="changeView(key)">{{ genre }} </b-dropdown-item>
      </b-dropdown>
    </div>

    <div>
      
    </div>
  </div>
</template>

<script>
export default {
  created() {
    this.getMovies();
  },
  data() {
    return {
      movies: [],
      selectedGenre: "전체",
      showGenre: [true, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false],
      sorted_movies: {
        "전체": {
          "vote_average": [],
          "vote_count": [],
          "popular": [],
          "like_users": [],
          "release_date": [],
        },
        "모험": {
          "vote_average": [],
          "vote_count": [],
          "popular": [],
          "like_users": [],
          "release_date": [],
        },
        "판타지": {
          "vote_average": [],
          "vote_count": [],
          "popular": [],
          "like_users": [],
          "release_date": [],
        },
        "애니메이션": {
          "vote_average": [],
          "vote_count": [],
          "popular": [],
          "like_users": [],
          "release_date": [],
        },
        "드라마": {
          "vote_average": [],
          "vote_count": [],
          "popular": [],
          "like_users": [],
          "release_date": [],
        },
        "공포": {
         "vote_average": [],
          "vote_count": [],
          "popular": [],
          "like_users": [],
          "release_date": [],
        },
        "액션": {
         "vote_average": [],
          "vote_count": [],
          "popular": [],
          "like_users": [],
          "release_date": [],
        },
        "코미디": {
         "vote_average": [],
          "vote_count": [],
          "popular": [],
          "like_users": [],
          "release_date": [],
        },
        "역사": {
         "vote_average": [],
          "vote_count": [],
          "popular": [],
          "like_users": [],
          "release_date": [],
        },
        "서부": {
          "vote_average": [],
          "vote_count": [],
          "popular": [],
          "like_users": [],
          "release_date": [],
        },
        "스릴러": {
         "vote_average": [],
          "vote_count": [],
          "popular": [],
          "like_users": [],
          "release_date": [],
        },
        "범죄": {
         "vote_average": [],
          "vote_count": [],
          "popular": [],
          "like_users": [],
          "release_date": [],
        },
        "다큐멘터리": {
          "vote_average": [],
          "vote_count": [],
          "popular": [],
          "like_users": [],
          "release_date": [],
        },
        "SF": {
          "vote_average": [],
          "vote_count": [],
          "popular": [],
          "like_users": [],
          "release_date": [],
        },
        "미스터리": {
          "vote_average": [],
          "vote_count": [],
          "popular": [],
          "like_users": [],
          "release_date": [],
        },
        "음악": {
          "vote_average": [],
          "vote_count": [],
          "popular": [],
          "like_users": [],
          "release_date": [],
        },
        "로맨스": {
         "vote_average": [],
          "vote_count": [],
          "popular": [],
          "like_users": [],
          "release_date": [],
        },
        "가족": {
          "vote_average": [],
          "vote_count": [],
          "popular": [],
          "like_users": [],
          "release_date": [],
        },
        "전쟁": {
          "vote_average": [],
          "vote_count": [],
          "popular": [],
          "like_users": [],
          "release_date": [],
        },
        "TV 영화": {
          "vote_average": [],
          "vote_count": [],
          "popular": [],
          "like_users": [],
          "release_date": [],
        },
      },
    };
  },
  methods: {
    onSlideStart(slide) {
      this.sliding = true;
      console.log(slide);
    },
    onSlideEnd(slide) {
      this.sliding = false;
      console.log(slide);
    },
    getMovies() {
      this.$store.dispatch("getMovies");
      this.movies = this.$store.state.movies;

      for (var i = 0; i < this.movies.length; ++i) {
        this.sorted_movies["전체"]["vote_average"].push(this.movies[i]);
        this.sorted_movies["전체"]["vote_count"].push(this.movies[i]);
        this.sorted_movies["전체"]["popular"].push(this.movies[i]);
        this.sorted_movies["전체"]["like_users"].push(this.movies[i]);
        this.sorted_movies["전체"]["release_date"].push(this.movies[i]);
        for (var j = 0; j < this.movies[i].genre_ids.length; ++j) {
          const gen = this.movies[i].genre_ids[j].name;
          this.sorted_movies[gen]["vote_average"].push(this.movies[i]);
          this.sorted_movies[gen]["vote_count"].push(this.movies[i]);
          this.sorted_movies[gen]["popular"].push(this.movies[i]);
          this.sorted_movies[gen]["like_users"].push(this.movies[i]);
          this.sorted_movies[gen]["release_date"].push(this.movies[i]);
        }
      }

      for (let gen in this.sorted_movies) {
        this.sorted_movies[gen]["vote_average"].sort(
          () => this.sorted_movies[gen].vote_average
        );
        this.sorted_movies[gen]["vote_count"].sort(
          () => this.sorted_movies[gen].vote_count
        );
        this.sorted_movies[gen]["popular"].sort(
          () => this.sorted_movies[gen].popular
        );
        this.sorted_movies[gen]["like_users"].sort(
          () => this.sorted_movies[gen].like_users.length
        );
        this.sorted_movies[gen]["release_date"].sort(
          () => this.sorted_movies[gen].release_date
        );
      }
    },
    changeView(genre_number) {
      if(genre_number){
        return
      }
    }
  },
};
</script>
<style scoped>
#recommend2 {
  padding: 2rem 10%;
  color: #fff;
}
</style>
