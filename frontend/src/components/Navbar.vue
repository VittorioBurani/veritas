<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
<nav class="navbar navbar-expand-lg">
  <div class="container justify-content-between mx-0 px-0">
    <div class="content-wrapper ms-4">
      <cite>
        <a href="https://vuejs.org/">
          <img class="navbar-logo me-2" src="@/assets/logo.svg" alt="Vue.js logo. Author: https://vuejs.org/">
        </a>
      </cite>
      <RouterLink class="navbar-brand" :to="{ name: 'home' }">
          Veritas
      </RouterLink>
    </div>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav mx-auto btn-group" role="group" aria-label="Basic radio toggle button group">
        <li class="nav-item">
            <RouterLink class="nav-link" :to="{ name: 'about' }">
                About
            </RouterLink>
        </li>
      </ul>
      <ul class="navbar-nav me-4">
        <li class="nav-item">
            <RouterLink class="nav-link" :to="{ name: 'about' }">
                About
            </RouterLink>
        </li>
      </ul>
    </div>
  </div>
</nav>
</template>

<style scoped>
.navbar {
  background: #e9e3ba;
}

a:link {
    color: #5b011b;
}

a:visited {
    color: #5b011b;
}

a:hover {
    color: #8d1638;
}

a:active {
    color: #8d1638;
}
</style>
