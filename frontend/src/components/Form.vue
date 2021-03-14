<template>
    <form>
    <v-text-field
      v-model="name"
      label="Podziel zakupy na kategorie"
    ></v-text-field>
    <v-select
      return-object
      v-model="select"
      label="Wybierz kolor"
      :items="items"
      :color="select.value"
    ></v-select>
    
    <v-btn
      class="mr-4"
      :disabled="!isValid"
      @click="addCategory"
    >
      Dodaj
    </v-btn>
  </form>
</template>

<script>



export default {
    data() {
        return {
            name: "",

            select: {
                 text: "",
                 value: ""
            },

            isValid: false,

            items: [
                {
                 text: "Czerwony",
                 value: "red",
                },
                {
                 text: "Różowy",
                 value: "pink",
                },
                {
                 text: "Fioletowy",
                 value: "purple",
                },
                {
                 text: "Niebieski",
                 value: "blue",               
                },
                {
                 text: "Zielony",
                 value: "green",                
                },
                {
                 text: "Pomarańczowy",
                 value: "orange",
                },
                
      ],
        }
    },

    methods: {
        addCategory() {
            const newCategory = {
                name: this.name,
                color: this.select.value,
                products: []
            }

            this.$store.commit("addNewCategory", newCategory)
            this.name = ""
            this.select = ""
        }
    },

    watch: {
        select() {
            if(this.select != "" && this.name != "") {
                this.isValid = true
            }
            else {
                this.isValid = false
            }
        },

        name() {
            if(this.select.value != "" && this.name != "") {
                this.isValid = true
            }
            else {
                this.isValid = false
            }
        }
    }
}
</script>


<style lang="scss">
    .red {
        color: #F44336;
    }
</style>