<template>
  <div class="about">
    <div v-if="savedLists.length > 0">
        <h1 class="mx-5 mt-5 pa-6 pb-0 text-h5">Tutaj znajdziesz zapisane listy:</h1>
        <div class="grid">
            <v-card
                class="mx-5 mt-6 card "
                max-width="344"
                v-for="(item, i) in savedLists" :key="i"
            >
                <v-card-text>
                <p class="display-1 text--primary">
                    {{item.name}}
                </p>
                <p>Utworzona: </p>
                </v-card-text>
                <v-card-actions>
                <router-link to="/lista">
                <v-btn
                    text
                    color="deep-purple accent-4"
                    @click="commitList(item)"
                >
                    Otwórz
                </v-btn>
                </router-link>
                <v-btn
                    text
                    color="deep-purple accent-4"
                >
                    Edytuj
                </v-btn>
                <v-btn
                    text
                    color="deep-purple accent-4"
                >
                    Usuń
                </v-btn>
                </v-card-actions>
            </v-card>
        </div>
    </div>
    <div v-else>
        <v-alert
        class="alert"
        text
        dense
        color="teal"
        icon="mdi-clock-fast"
        border="left"
        >
        Nie masz obecnie zapisanej żadnej listy zakupowej. Kliknij w przycisk żeby przejść do kreatora listy.
        </v-alert>
            
            <router-link to="/" class="btn v-btn v-btn--has-bg theme--light v-size--default primary">
            Przejdź
            </router-link>
            
    </div>
  </div>
</template>


<script>

import { mapState } from 'vuex'

export default {
    data() { 
        return {
            haveSavedList: false,
        }
    },
    computed: {
        ...mapState(["savedLists"]),
    },
    methods: {
        commitList(item) {
            this.$store.commit("changeOpenList", item)
        }
    }
    
}
</script>

<style lang="scss" scoped>
    .alert {
        width: 95%;
        margin: 50px auto 30px;
    }
    .btn {
        color: #222;
        margin: 0 auto;
        display: block;
    }
    .grid {
        padding: 30px;
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr;

        .card {
            padding: 20px;
            width: 300px;
        }
    }

    a {
        color: white !important;
        text-decoration: none;
        width: 110px;
        text-align: center;
        vertical-align: middle;
        line-height: 36px;
    }
</style>