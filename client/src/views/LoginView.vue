<template>
  <div id="login">
    <section class="vh-100 gradient-custom">
      <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
          <div class="col-12 col-md-8 col-lg-6 col-xl-5">
            <div class="card bg-dark text-white" style="border-radius: 1rem">
              <div class="card-body p-5 text-center">
                <div class="mb-md-5 mt-md-4 pb-5">
                  <h2 class="fw-bold mb-2 text-uppercase">Login</h2>
                  <p class="text-white-50 mb-5">
                    로그인을 위한 아이디와 비밀번호를 입력해주세요.
                  </p>
                  <form @submit.prevent="logIn">
                    <div class="form-outline form-white mb-4">
                      <input
                        type="text"
                        id="username"
                        v-model="username"
                        class="form-control form-control-lg"
                        placeholder="아이디"
                      />
                    </div>

                    <div class="form-outline form-white mb-4">
                      <input
                        type="password"
                        id="password"
                        v-model="password"
                        class="form-control form-control-lg"
                        placeholder="비밀번호"
                      />
                    </div>

                    <!-- <p class="small mb-5 pb-lg-2">
                    <a class="text-white-50" href="#!">Forgot password?</a>
                  </p> -->

                    <button
                      class="btn btn-outline-light btn-lg px-5"
                      type="submit"
                    >
                      로그인
                    </button>
                  </form>
                  <!-- <div
                    class="d-flex justify-content-center text-center mt-4 pt-1"
                  >
                    <a href="#!" class="text-white"
                      ><i class="fab fa-facebook-f fa-lg"></i
                    ></a>
                    <a href="#!" class="text-white"
                      ><i class="fab fa-twitter fa-lg mx-4 px-2"></i
                    ></a>
                    <a href="#!" class="text-white"
                      ><i class="fab fa-google fa-lg"></i
                    ></a>
                  </div> -->
                </div>

                <div>
                  <p class="mb-0">
                    계정이 없으신가요?
                    <a href="/signup" class="text-white-50 fw-bold">회원가입</a>
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script>
export default {
data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password


      const payload = {
        username, password
      }
      this.$store.dispatch('logIn',payload)
    },
  },

};
</script>
<style scoped>
.gradient-custom {
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
</style>
