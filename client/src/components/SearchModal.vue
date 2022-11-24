<template>
  <div>
    <b-modal id="searchModal" title="검색" hide-footer size="xl">
      <b-container fluid>
        <b-row class="my-1">
          <b-col sm="10">
            <b-form-input
              id="input-default"
              placeholder="원하는 영화를 검색해보세요"
              v-model="word"
              @input="searchWord"
            ></b-form-input>
          </b-col>
          <b-col sm="2">
            <b-button>검색</b-button>
          </b-col>
        </b-row>
      </b-container>
      <hr />
      <div>
        <b-button v-b-toggle.collapse-1>필터</b-button>
        <b-collapse id="collapse-1" class="mt-2">
          <b-card>
            <b-row>
              <b-col>
                <div>
                  <b-button class="mr-1 mb-1"
                    v-for="(genre, idx) in genres"
                    :key="idx"
                    @click="addGenre(genre.name)"
                    >{{ genre.name }}</b-button
                  >
                </div>
              </b-col>
            </b-row>
          </b-card>
        </b-collapse>
      </div>
      <div>
        <div>
          <span class="mr-2">검색결과</span>

          <span v-if="selectedGenres.length > 0"
            ><b-button class="mr-1" v-for="(selected, idx) in selectedGenres" :key="idx" @click="deleteGenre(selected)">{{
              selected
            }}</b-button></span
          >
        </div>
        <div class="contain">
              <b-card
              class="poster"
              v-for="movie in rec_movies" :key="movie.id"
                :img-src= "baseUrl + movie.poster_path"
                img-alt="Image"
                overlay
                @click="moveToDetail(movie.id)"
              ></b-card
            >

        </div>
      </div>
    </b-modal>
  </div>
</template>

<script>
export default {
  created() {},
  props: ["movies", "genres"],
  data() {
    return {
      selectedGenres: [],
      word: "",
      rec_movies: [],
      imgPoster: "",
      baseUrl: 'https://image.tmdb.org/t/p/original'
    };
  },
  methods: {
    searchWord() {
      if (!this.word.replace(/ /g, "")) {
        this.rec_movies = [];
        return;
      }
      this.rec_movies = this.movies.filter(
        (movie) =>
          movie.title.replace(/ /g, "").includes(this.word.replace(/ /g, "")) ||
          movie.original_title
            .replace(/ /g, "")
            .includes(this.word.replace(/ /g, ""))
      );

      if (this.selectedGenres.length>0){
        let flag=0
        for (let i=this.rec_movies.length-1;i>=0;--i){
          for (let j=0;j<this.rec_movies[i].genre_ids.length;++j){
            if (this.selectedGenres.includes(this.rec_movies[i].genre_ids[j].name)){
              flag=1
              break
            }
          }
          if (!flag) this.rec_movies.splice(i,1)
        }
      }

    },
    addGenre(genre_name){
      if (this.selectedGenres.includes(genre_name)) return
      this.selectedGenres.push(genre_name)
      this.searchWord()
    },
    deleteGenre(genre_name){
      for (let i=0;i<this.selectedGenres.length;++i){
        if (this.selectedGenres[i]==genre_name){
          this.selectedGenres.splice(i,1)
        }
      }
      this.searchWord()
    },
    moveToDetail(id){
      this.$router.push({name:'detail', params: {movie_id: id}})
      window.location.reload();
    }
  },
};
</script>
<style scoped>
.contain {
  display: grid;
  grid-template-columns: repeat(6,1fr);
}
.poster{
  cursor: pointer;
}
</style>