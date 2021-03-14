<template>
    <div>
        <div class="input mt-4">
            <v-text-field v-model="product" class="product mx-2"
            label="Dodaj produkt"
            ></v-text-field>
            <v-text-field v-model="quantity" class="quantity mx-2"
            label="Wybierz ilość"
            ></v-text-field>
            <v-select class="type mx-2"
                :items="items"
                label="Jednostka"
                v-model="select"
            ></v-select>
            <v-btn
            class="mx-2"
            fab
            dark
            small
            color="primary"
            @click="addProduct"
            >
                <v-icon dark >
                    mdi-plus
                </v-icon>
            </v-btn>
        </div>
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
                    </tr>
                </thead>
                <tbody>
                     <tr
                    v-for="(product, i) in products" :key="i" class="px-2 height"
                    >
                    <td class="product">{{ product.product }}</td>
                    <td class="quantity">{{product.quantity }} &nbsp; {{ product.type }}
                        <v-icon class="ico" @click="remove(i)">
                            mdi-close
                        </v-icon>
                    </td>
                    
                    </tr>
                </tbody>
                </template>
            </v-simple-table>
        </div>
    </div>
</template>

<script>
import { mapState } from 'vuex'

  export default {
    data: () => ({
      items: ['g', 'kg', 'opakowanie', 'szt', 'ml', 'l'],
      product: "",
      quantity: "",
      select: "",
    }),

    computed: {
         ...mapState(["lists"]),

         products() {
             return this.lists[this.index].products
         }
    },

    props: ["index"],
    
    methods: {
        addProduct() {
            if(this.product != "" && this.quantity != "" &&  this.select != "") {
                const newProduct = {
                product: this.product,
                quantity: this.quantity,
                type: this.select
                }
                this.$store.commit("addProduct", { newProduct, index: this.index })

                this.product = ""
                this.quantity = ""  
                this.select = ""
            }
        },

        remove(i) {
          this.$store.commit("removeProduct", { index: this.index, i,})
      }, 
    }
  }
</script>

<style lang="scss" scoped>
    .input {
        display:flex;
        justify-content: space-between;
        align-items: center;

        .product {
            width: 40%;
        }

        .quantity {
            width: 10%
        }
        .type {
            width: 10%
        }
        .btn {
            cursor: pointer;
            font-size: 30px;

            &:hover {
                transform: scale(1.1);
            }   
        }
    }

    .height {
        min-height: 48px !important;
    }

    .cap {
        text-transform: capitalize;
        display: flex;
        justify-content: space-between;
        vertical-align: middle;
        cursor: pointer;

        span {
            text-transform: none;
            color: gray
        }

        button {
            color: white;
            cursor: pointer;
            font-size: 28px;
        }
    }

    .cap:hover button{
       color: black
    }
    
    .ico {
        float: right;
    }

    .product {
        width: 70%;
    }
    .quantity {
        width: 30%;
    }
</style>