<template>
  <div id="app">
    <Navbar />
    <router-view />
  </div>
</template>

<script>
import Navbar from "@/components/shared/Navbar";

export default {
  components: { Navbar }
};
</script>

<style lang="scss">
body {
  min-height: 100vh;
  background-image: linear-gradient(
    to bottom,
    #1e1e2e,
    #1e1e2c,
    #1e1e29,
    #1e1e27,
    #1e1e24
  );
  background-color: #2f3542;
}
</style>
