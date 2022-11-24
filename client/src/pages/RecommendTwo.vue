<template>
  <div>
    <b-carousel
      id="carousel-1"
      v-model="slide"
      :interval="4000"
      controls
      indicators
      background="#ababab"
      img-width="1024"
      img-height="480"
      style="text-shadow: 1px 1px 2px #333;"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >
      <!-- Text slides with image -->



      
      <b-carousel-slide
        caption="First slide"
        text="Nulla vitae elit libero, a pharetra augue mollis interdum."
        img-src="https://picsum.photos/1024/480/?image=52"
      ><div>
      <b-card img-src="https://picsum.photos/400/400/?image=41" img-alt="Image" overlay>
      </b-card>
      <b-card img-src="https://picsum.photos/400/400/?image=41" img-alt="Image" overlay></b-card>
      <b-card img-src="https://picsum.photos/400/400/?image=41" img-alt="Image" overlay></b-card>
      </div>
      </b-carousel-slide>

      <!-- Slides with custom text -->
      <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=54">
        <h1>Hello world!</h1>
      </b-carousel-slide>

      <!-- Slides with image only -->
      <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=58"></b-carousel-slide>

      <!-- Slides with img slot -->
      <!-- Note the classes .d-block and .img-fluid to prevent browser default image alignment -->
      <b-carousel-slide>
        <template #img>
          <img
            class="d-block img-fluid w-100"
            width="1024"
            height="480"
            src="https://picsum.photos/1024/480/?image=55"
            alt="image slot"
          >
        </template>
      </b-carousel-slide>

      <!-- Slide with blank fluid image to maintain slide aspect ratio -->
      <b-carousel-slide caption="Blank Image" img-blank img-alt="Blank image">
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse eros felis, tincidunt
          a tincidunt eget, convallis vel est. Ut pellentesque ut lacus vel interdum.
        </p>
      </b-carousel-slide>
    </b-carousel>

    <p class="mt-4">
      Slide #: {{ slide }}<br>
      Sliding: {{ sliding }}
    </p>
  </div>
</template>

<script>
  export default {
    created(){
      this.getMovies()
    },
    data() {
      return {
        slide: 0,
        sliding: null,
        movies:[],
        sorted_movies:{
          '전체':{
            'vote_average':[],
            'vote_count':[],
            'popular':[],
            'like_users':[],
            'release_date':[],
          },
          '모험':{
            'vote_average':[],
            'vote_count':[],
            'popular':[],
            'like_users':[],
            'release_date':[],
            },
          '판타지':{
            'vote_average':[],
            'vote_count':[],
            'popular':[],
            'like_users':[],
            'release_date':[],
            },
          '애니메이션':{
            'vote_average':[],
            'vote_count':[],
            'popular':[],
            'like_users':[],
            'release_date':[],
            },
          '드라마':{
            'vote_average':[],
            'vote_count':[],
            'popular':[],
            'like_users':[],
            'release_date':[],
            },
          '공포':{
            'vote_average':[],
            'vote_count':[],
            'popular':[],
            'like_users':[],
            'release_date':[],
            },
          '액션':{
            'vote_average':[],
            'vote_count':[],
            'popular':[],
            'like_users':[],
            'release_date':[],
            },
          '코미디':{
            'vote_average':[],
            'vote_count':[],
            'popular':[],
            'like_users':[],
            'release_date':[],
            },
          '역사':{
            'vote_average':[],
            'vote_count':[],
            'popular':[],
            'like_users':[],
            'release_date':[],
            },
          '서부':{
            'vote_average':[],
            'vote_count':[],
            'popular':[],
            'like_users':[],
            'release_date':[],
            },
          '스릴러':{
            'vote_average':[],
            'vote_count':[],
            'popular':[],
            'like_users':[],
            'release_date':[],
            },
          '범죄':{
            'vote_average':[],
            'vote_count':[],
            'popular':[],
            'like_users':[],
            'release_date':[],
            },
          '다큐멘터리':{
            'vote_average':[],
            'vote_count':[],
            'popular':[],
            'like_users':[],
            'release_date':[],
            },
          'SF':{
            'vote_average':[],
            'vote_count':[],
            'popular':[],
            'like_users':[],
            'release_date':[],
            },
          '미스터리':{
            'vote_average':[],
            'vote_count':[],
            'popular':[],
            'like_users':[],
            'release_date':[],
            },
          '음악':{
            'vote_average':[],
            'vote_count':[],
            'popular':[],
            'like_users':[],
            'release_date':[],
            },
          '로맨스':{
            'vote_average':[],
            'vote_count':[],
            'popular':[],
            'like_users':[],
            'release_date':[],
            },
          '가족':{
            'vote_average':[],
            'vote_count':[],
            'popular':[],
            'like_users':[],
            'release_date':[],
            },
          '전쟁':{
            'vote_average':[],
            'vote_count':[],
            'popular':[],
            'like_users':[],
            'release_date':[],
            },
          'TV 영화':{
            'vote_average':[],
            'vote_count':[],
            'popular':[],
            'like_users':[],
            'release_date':[],
            },
          }
      }
    },
    methods: {
      onSlideStart(slide) {
        this.sliding = true
        console.log(slide)
      },
      onSlideEnd(slide) {
        this.sliding = false
        console.log(slide)
      },
      getMovies(){
        this.$store.dispatch('getMovies')
        this.movies=this.$store.state.movies

          
        for (var i=0;i<this.movies.length;++i){
          this.sorted_movies['전체']['vote_average'].push(this.movies[i])
          this.sorted_movies['전체']['vote_count'].push(this.movies[i])
          this.sorted_movies['전체']['popular'].push(this.movies[i])
          this.sorted_movies['전체']['like_users'].push(this.movies[i])
          this.sorted_movies['전체']['release_date'].push(this.movies[i])
          for (var j=0;j<this.movies[i].genre_ids.length;++j){
            const gen=this.movies[i].genre_ids[j].name
            this.sorted_movies[gen]['vote_average'].push(this.movies[i])
            this.sorted_movies[gen]['vote_count'].push(this.movies[i])
            this.sorted_movies[gen]['popular'].push(this.movies[i])
            this.sorted_movies[gen]['like_users'].push(this.movies[i])
            this.sorted_movies[gen]['release_date'].push(this.movies[i])
          }
        }
        
        for (let gen in this.sorted_movies){
          this.sorted_movies[gen]['vote_average'].sort(()=>this.sorted_movies[gen].vote_average)
          this.sorted_movies[gen]['vote_count'].sort(()=>this.sorted_movies[gen].vote_count)
          this.sorted_movies[gen]['popular'].sort(()=>this.sorted_movies[gen].popular)
          this.sorted_movies[gen]['like_users'].sort(()=>this.sorted_movies[gen].like_users.length)
          this.sorted_movies[gen]['release_date'].sort(()=>this.sorted_movies[gen].release_date)
        }
      },
    
    }
  }
</script>