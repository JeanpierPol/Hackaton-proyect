<template>
  <div id="app">
    <Nav></Nav>
    <div id="main">
      <router-view />
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
// @ is an alias to /src
import Nav from "@/views/_common/Nav.vue";
import Footer from "@/views/_common/Footer.vue";

export default {
  name: "App",
  components: {
    Nav,
    Footer,
  },
};
</script>

<style>
#main {
  flex: 1;
}
</style>
