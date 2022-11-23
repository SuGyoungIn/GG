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
        <b-button v-b-toggle.collapse-1>상세설정</b-button>
        <b-collapse id="collapse-1" class="mt-2">
          <b-card>
            <b-row>
              <b-col sm="9">
                <p class="card-text">장르</p>
                <div>
                  <b-button
                    v-for="(genre, idx) in genres"
                    :key="idx"
                    @click="addGenre(genre)"
                    >{{ genre }}</b-button
                  >
                </div>
              </b-col>
              <b-col sm="3">
                <p class="card-text">별점</p>
              </b-col>
            </b-row>
          </b-card>
        </b-collapse>
      </div>
      <div>
        <div>
          <span>검색결과</span>

          <span v-if="selectedGenres.length > 0"
            ><b-button v-for="(selected, idx) in selectedGenres" :key="idx">{{
              selected
            }}</b-button></span
          >
        </div>
        <b-container>
          <b-row>
            <b-col
              ><b-card
                img-src="https://picsum.photos/400/400/?image=41"
                img-alt="Image"
                overlay
              ></b-card
            ></b-col>
            <b-col
              ><b-card
                img-src="https://picsum.photos/400/400/?image=41"
                img-alt="Image"
                overlay
              ></b-card
            ></b-col>
            <b-col
              ><b-card
                img-src="https://picsum.photos/400/400/?image=41"
                img-alt="Image"
                overlay
              ></b-card
            ></b-col>
            <b-col
              ><b-card
                img-src="https://picsum.photos/400/400/?image=41"
                img-alt="Image"
                overlay
              ></b-card
            ></b-col>
            <b-col
              ><b-card
                img-src="https://picsum.photos/400/400/?image=41"
                img-alt="Image"
                overlay
              ></b-card
            ></b-col>
            <b-col
              ><b-card
                img-src="https://picsum.photos/400/400/?image=41"
                img-alt="Image"
                overlay
              ></b-card
            ></b-col>
          </b-row>
        </b-container>
      </div>
    </b-modal>
  </div>
</template>

<script>
export default {
  created() {},
  props:[],
  data(){
    return{
      genres: [],
      selectedGenres: [],
      word:'',
      
    }
  },
  methods: {
    searchWord(){
      
    }
  }
}
</script>