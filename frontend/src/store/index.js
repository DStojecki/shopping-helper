import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    lists: [{
        color: "green",
        name: "Warzywa i owoce",
        products: [],
    },
    {
        color: "pink",
        name: "Mięso i wędliny",
        products: [],
    },
    {
        color: "red",
        name: "Chemia",
        products: [],
    }],
    isLogged: false,
    savedLists: [{
        list: [{
            color: "green",
            name: "Warzywa i owoce",
            products: [{
                product: "nazwa",
                quantity: "23",
                type: "g"
            },
            {
                product: "nazwa",
                quantity: "23",
                type: "g"
            },
            {
                product: "nazwa",
                quantity: "23",
                type: "g"
            }],
        },
        {
            color: "pink",
            name: "Mięso i wędliny",
            products: [],
        },
        {
            color: "red",
            name: "Chemia",
            products: [],
        }],
        name: "lista testowa"
    }],
    openList: [],
  },

  mutations: {
    addNewCategory(state, payload) {
        state.lists.push(payload)
    },

    removeCategory(state, payload) {
        state.lists.splice(payload, 1);
    },

    removeProduct(state, payload) {
        state.lists[payload.index].products.splice(payload.i, 1)
    },

    changeIsLogged(state, payload) {
        state.isLogged = payload
    },

    addProduct(state, payload) {
        state.lists[payload.index].products.push(payload.newProduct)
    },

    addNewList(state, payload) {
        state.savedLists.push({
            name: payload,
            list: state.lists
        })
        state.lists = []
    },
    changeOpenList(state, payload) {
        state.openList = payload
    },
},

  actions: {
  },
  modules: {
  }
})
