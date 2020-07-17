<template>
  <b-navbar type="is-dark">
    <template slot="brand">
      <b-navbar-item tag="div" :to="{ path: '/' }">
        <img
          src="@/assets/logo_dark.png"
          alt="Movimento União Rio"
          class="logo"
        />
        <h5 class="title is-5">
          Monitoramento União Rio
        </h5>
      </b-navbar-item>
    </template>

    <template slot="start">
      <b-navbar-item tag="router-link" :to="{ name: 'Home' }">
        Início
      </b-navbar-item>
      <!-- <b-navbar-item tag="router-link" :to="{ name: 'Projections' }">
        Projeções
      </b-navbar-item> -->
    </template>
  </b-navbar>
</template>

<style lang="scss">
.logo {
  display: block;
  max-height: 10vh !important;
  height: 2.5rem;
}

.title {
  margin-left: 1rem;
}
</style>
