<template>
<div>
    <h1 class="pa-6 pb-0 text-h4 text-capitalize">{{ openList.name }}</h1>
    <v-expansion-panels
      multiple
      focusable
      expand-icon 
      class="pa-6">
        <v-expansion-panel class="my-1"
            v-for="(item,i) in boughtList.list" :key="i">
            <v-expansion-panel-header class="white-font" :class="item.color">{{ item.name }} 
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <div>
                        <v-simple-table dense>
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
                                v-for="(product, i) in item.products" :key="i" class="px-2 height"
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
        </v-expansion-panel>
    </v-expansion-panels>
</div>
</template>

<script>
import { mapState } from "vuex"

export default {
    computed: {
        ...mapState(["boughtList",])
    },
    props: ["name"],
    
}
</script>

<style lang="scss" scoped>
    .white-font {
        color: white !important;
    }
</style>