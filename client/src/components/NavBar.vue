<template>
  <div>
<nav class="navbar navbar-expand-lg navbar-light bg-light py-3">
      <!-- Container wrapper -->
      <div class="container-fluid">
        <!-- Collapsible wrapper -->
        <div class="" id="navbarSupportedContent">
          <!-- Navbar brand -->
          <router-link to="/"
            ><img src="/LOGO.png" alt="logo" style="width: 100px"
          /></router-link>
          <!-- Left links -->
        </div>

        <!-- Right elements -->
        <div class="d-flex align-items-center">
          <!-- Icon -->
          <router-link class="mx-2" to="/community">커뮤니티</router-link>
          <router-link class="mx-2" to="/login" v-if="!isLogin"
            >로그인</router-link
          >
          <router-link class="mx-2" to="/signup" v-if="!isLogin"
            >회원가입</router-link
          >
          <b-nav-item-dropdown :text="username" v-if="isLogin">
            <b-dropdown-item @click="movePage(myPage)"
              >마이페이지</b-dropdown-item
            >
            <b-dropdown-item @click="logOut">로그아웃</b-dropdown-item>
          </b-nav-item-dropdown>

          <span class="mx-2" v-b-modal.searchModal>
            <img src="/img/search.png" alt="검색" />
          </span>
          <!-- Avatar -->
        </div>
        <!-- Right elements -->
      </div>
      <!-- Container wrapper -->
    </nav>
  </div>
</template>