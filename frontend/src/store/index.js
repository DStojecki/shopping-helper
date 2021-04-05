import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    list: [{
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
    savedLists: [],
    openList: [],
    boughtList: [],
    requestedListId: 0,
    editable: false,
  },

  mutations: {
    
    changeList(state, payload) {
        state.list = payload
    },

    cleanList(state) {
        state.list = []
    },

    addNewCategory(state, payload) {
        state.list.push(payload)
    },

    removeCategory(state, payload) {
        state.list.splice(payload, 1);
    },

    removeProduct(state, payload) {
        state.list[payload.index].products.splice(payload.i, 1)
    },

    changeIsLogged(state, payload) {
        state.isLogged = payload
    },

    addProduct(state, payload) {
        state.list[payload.index].products.push(payload.newProduct)
    },
    
    addToBoughtList(state, payload) {
        state.boughtList.push(payload)
    },

    changeId(state, payload) {
        state.requestedListId = payload
    },

    changeEditable(state, paylod) {
        state.editable = paylod
    }
},

  actions: {
  },
  modules: {
  }
})
