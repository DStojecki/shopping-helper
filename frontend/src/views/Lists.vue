<template>
  <div class="about">
    <div v-if="savedLists.length > 0">
        <h1 class="mx-5 mt-5 pa-6 pb-0 text-h5">Tutaj znajdziesz zapisane listy:</h1>
        <div class="grid">
            <v-card
                class="mx-5 mt-6 card "
                max-width="344"
                v-for="(item) in savedLists" :key="item.id"
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
                    @click="openList(item.id)"
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
                    @click="deleteList(item.id)"
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

export default {
    data() { 
        return {
            haveSavedList: false,
            savedLists: [],
        }
    },

    methods: {
        openList(id) {
            this.$store.commit("changeId", id)
        },

        downloadList() {
            this.axios.get('http://localhost/api/lists',{ 

            headers: {'Authorization': `Bearer ${localStorage.getItem('access_token')}`}

            }).then((res) => {
                this.savedLists = res.data.results
            })
        },

        deleteList(id) {
            this.axios.delete(`http://localhost/api/lists/${id}`,{ 

            headers: {'Authorization': `Bearer ${localStorage.getItem('access_token')}`}

            }).then((res) => {
                this.savedLists = res.data.results
                this.downloadList()
            })
        }
    },

    created() {
        this.downloadList()
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

    .list {
        list-style: none;
        padding: 30px;

        li {
            border: 1px solid #999;
            border-radius: 2px;
            width: 100%;
            margin: 0 auto;
            padding: 10px 15px;
            
            span {
                margin: 0px 10px;
            }
        }
    }
</style>