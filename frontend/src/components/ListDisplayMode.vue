<template>
<div>
    <h1 class="pa-6 pb-0 text-h5 text-capitalize">{{ openList.name }}</h1>
    <v-expansion-panels
      multiple
      focusable
      expand-icon 
      class="pa-6">
        <v-expansion-panel class="my-1"
            v-for="(item,i) in openList.list" :key="i" >
            <v-expansion-panel-header class="white-font" :class="item.color">{{ item.name }} 
                </v-expansion-panel-header>
                <v-expansion-panel-content v-if="item.products.length > 0">
                    <div >
                        <v-simple-table dense >
                            <template v-slot:default>
                            <thead>
                                <tr>
                                <th class="text-left">
                                    Nazwa
                                </th>
                                <th class="text-left">
                                    Ilość
                                </th>
                                <th></th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr
                                v-for="(product, index) in item.products" :key="index" class="px-2 height"
                                >
                                <td class="product">{{ product.product }}</td>
                                <td class="quantity">
                                    {{ product.quantity }} &nbsp; {{ product.type }}
                                </td>
                                <td class="button">
                                    <v-btn
                                        color="green"
                                        dark
                                        class="float-right my-1"
                                        @click="addToBought(i, index)"
                                        
                                    >
                                        <v-icon dark>
                                        mdi-cart-variant
                                        </v-icon>
                                    </v-btn>
                                </td>
                               
                                </tr>
                            </tbody>
                            </template>
                        </v-simple-table>
                    </div>
                </v-expansion-panel-content>
                <v-expansion-panel-content v-else>
                    <p class="mt-2 mb-0">Ta kategoria jest pusta.</p>
                </v-expansion-panel-content>
        </v-expansion-panel>
    </v-expansion-panels>
    <h1 class="pa-6 pb-0 text-h5 text-capitalize">Zakupione</h1>
    <v-simple-table dense class="pa-6" v-if="boughtList.length > 0">
        <template v-slot:default>
            <thead>
                <tr>
                    <th class="text-left">
                        Nazwa
                    </th>
                    <th class="text-left">
                        Ilość
                    </th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="px-2 height" v-for="(productBought, index) in boughtList" :key="index">
                        <td class="product">{{ productBought.product }}</td>
                        <td class="quantity"> {{ productBought.quantity }} {{ productBought.quantity }}
                        </td>
                    </tr>
                </tbody>
        </template>
    </v-simple-table>
    <p class="pa-6">Tutaj pojawi się lista rzeczy które już zostały wsadzone do koszyka. Żeby dodać produkt do listy produktów zakupionych kliknij zielony przycisk obok nazwy produktu.</p>

    <v-btn
    color="primary"
    dark class="create-btn mr-6 mb-4"
    >       Zakończ zakupy
    </v-btn>
</div>
</template>

<script>
import { mapState } from "vuex"

export default {
    computed: {
        ...mapState(["openList", "boughtList"])
    },
    props: ["name"],
    methods: {
        addToBought(i, index) {
            const product = this.openList.list[i].products[index]
            this.openList.list[i].products.splice(index, 1)
            this.$store.commit("addToBoughtList", product)
        }   
    }
    
}
</script>

<style lang="scss" scoped>
    .white-font {
        color: white !important;
    }
    .create-btn {
        margin-top: 40px;
        float: right;
        color: white;
    }
</style>