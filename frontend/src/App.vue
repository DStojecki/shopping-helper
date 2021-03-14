<template>
  <v-app id="inspire">
    <div v-if="isLogged">
    <v-navigation-drawer
      class="deep-purple accent-4"
      dark
      v-model="drawer"
      app
    >
      <v-list>
        <v-list-item
          v-for="item in items"
          :key="item.title"
          :to="item.to"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <template v-slot:append>
        <div class="pa-2">
          <v-btn block>
            Wyloguj
          </v-btn>
        </div>
      </template>
    </v-navigation-drawer>

    <v-app-bar
      app
      absolute
      color="#6A76AB"
      dark
      shrink-on-scroll
      prominent
      src="img/background.jpg"
      fade-img-on-scroll
      scroll-target="#scrolling-techniques-3"
    >
      <template v-slot:img="{ props }">
        <v-img
          v-bind="props"
          gradient="to top right, rgba(100,115,201,.7), rgba(25,32,72,.7)"
        ></v-img>
      </template>

      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-spacer></v-spacer>

      <template v-slot:extension>
        <v-tabs align-with-title>
          <v-tab>Lista</v-tab>
          <v-tab>Kupione</v-tab>
        </v-tabs>
      </template>
    </v-app-bar>

    <v-main>
      <router-view></router-view>
    </v-main>
    </div>
    <Login v-else />
  </v-app>
</template>

<script>

import Login from './views/Login'
import { mapState } from 'vuex'

  export default {
    data: () => ({ 
        drawer: null,
        items: [
          { title: 'Stwórz listę', icon: 'mdi-view-dashboard', to: "/"},
          { title: 'Listy', icon: 'mdi-format-list-bulleted-triangle', to: "/lists" },
          { title: 'Historia', icon: 'mdi-alpha-h-box', to: "/history"}
        ], 
        }),
    
    computed: {
        ...mapState(["isLogged"])
    },

    components: {
        Login,
    }
  }
</script>