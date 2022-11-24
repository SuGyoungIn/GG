<template>
  <div id="recommend2">
    <div class="d-flex justify-content-between">
      <h2>
        {{ selectedGenre }}
      </h2>
      <div>
      <b-dropdown text="장르 선택">
        <b-dropdown-item v-for="value,genre,key of sorted_movies" :key="key" @click="changeGenre(genre)">{{ genre }} </b-dropdown-item>
      </b-dropdown>
      <b-dropdown :text="filter">
        <b-dropdown-item @click="changeFilter(0)">평점 높은 순</b-dropdown-item>
        <b-dropdown-item @click="changeFilter(1)">평가 많은 순</b-dropdown-item>
        <b-dropdown-item @click="changeFilter(2)">인기도 순</b-dropdown-item>
        <b-dropdown-item @click="changeFilter(3)">좋아요 순</b-dropdown-item>
        <b-dropdown-item @click="changeFilter(4)">최신영화 순</b-dropdown-item>
      </b-dropdown>
      <b-dropdown :text="cnt +'개'">
        <b-dropdown-item @click="changeCnt(24)">24개 보기</b-dropdown-item>
        <b-dropdown-item @click="changeCnt(48)">48개 보기</b-dropdown-item>
        <b-dropdown-item @click="changeCnt(96)">96개 보기</b-dropdown-item>
        <b-dropdown-item @click="changeCnt(192)">192개 보기</b-dropdown-item>
        <b-dropdown-item @click="changeCnt(384)">384개 보기</b-dropdown-item>
      </b-dropdown>
      </div>
    </div>

    <div class="contain">
      <PosterCard v-for="(movie,idx) in on_view_movies" :key="idx" :movie="movie" />
    </div>
  </div>
</template>

<script>
import PosterCard from "../components/PosterCard.vue"
export default {
  created() {
    this.getMovies()
    this.changeGenre("전체")
  },
  components: {PosterCard},
  data() {
    return {
      movies: [],
      filter:"평점 높은 순",
      selectedGenre: "전체",
      selectedGenreMovies: [],
      on_view_movies:[],
      cnt:24,
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
          (a,b) => b.vote_average-a.vote_average
        );
        this.sorted_movies[gen]["vote_count"].sort(
          (a,b) => b.vote_count-a.vote_count
        );
        this.sorted_movies[gen]["popular"].sort(
          (a,b) => b.popular-a.popular
        );
        this.sorted_movies[gen]["like_users"].sort(
          (a,b) => b.like_users.length-a.like_users.length
        );
        this.sorted_movies[gen]["release_date"].sort(
          (a,b) => b.release_date-a.release_date
        );
        this.on_view_movies=this.selectedGenreMovies.slice(0,this.cnt)
      
      }
    },
    changeGenre(genre) {
      this.selectedGenreMovies = this.sorted_movies[genre]["vote_average"]
      this.selectedGenre = genre
      this.on_view_movies=this.selectedGenreMovies.slice(0,this.cnt)
      
    },
    changeFilter(filter) {
      console.log(filter)
      console.log(this.selectedGenreMovies)
      if(filter === 0){
        this.selectedGenreMovies = this.sorted_movies[this.selectedGenre]["vote_average"]
        this.filter = "평점 높은 순"
        console.log(this.selectedGenreMovies)
      } else if(filter === 1) {
        this.selectedGenreMovies = this.sorted_movies[this.selectedGenre]["vote_count"]
        this.filter = "평가 많은 순"
      } else if(filter === 2){
        this.selectedGenreMovies = this.sorted_movies[this.selectedGenre]["popular"]
        this.filter = "인기도 순"
      } else if(filter === 3) {
        this.selectedGenreMovies = this.sorted_movies[this.selectedGenre]["like_users"]
        this.filter = "좋아요 순"
      } else if(filter === 4) {
        this.selectedGenreMovies = this.sorted_movies[this.selectedGenre]["release_date"]
        this.filter = "최신영화 순"
      }

      this.on_view_movies=this.selectedGenreMovies.slice(0,this.cnt)
      
    },
    changeCnt(c){
      this.cnt=c
      this.on_view_movies=this.selectedGenreMovies.slice(0,this.cnt)

    }
  },
};
</script>
<style scoped>
#recommend2 {
  padding: 2rem 10%;
  color: #fff;
}
.contain{
  display: grid;
  grid-template-columns: repeat(6, 1fr);
}
</style>
