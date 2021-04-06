<template>
  <div class="container pt-12">
    <v-btn class="mx-2 btn" fab dark color="indigo" @click="collappse">
      <v-icon v-if="!isVisable" dark> mdi-minus </v-icon>
      <v-icon v-else dark> mdi-plus </v-icon>
    </v-btn>

    <Form class="active py-0 mb-8" />

    <div class="text-center d-flex pb-4 pt-4">
      <v-btn :disabled="disableButtons" @click="all"> Pokaż wszystkie </v-btn>
      <v-btn :disabled="disableButtons" @click="none" class="mx-4">
        Zamknij wszystkie
      </v-btn>
    </div>

    <v-expansion-panels v-model="panel" multiple focusable expand-icon>
      <v-expansion-panel class="my-1" v-for="(item, i) in list" :key="i">
        <v-expansion-panel-header class="white-font" :class="list[i].color"
          >{{ list[i].name }}
          <div class="ico">
            <v-icon
              class="delete-ico"
              color="white"
              @click.stop="openDialog(i)"
            >
              mdi-delete
            </v-icon>
          </div>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <List :index="i" />
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
    <v-dialog v-model="dialog" max-width="290">
      <v-card>
        <v-card-title class="headline"> Uwaga! </v-card-title>

        <v-card-text> Czy chcesz usunąć wybraną katagorię? </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn color="green darken-1" text @click="dialog = false">
            NIE
          </v-btn>

          <v-btn color="green darken-1" text @click="remove(index)">
            TAK
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="secondDialog" persistent max-width="600px">
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          v-if="isInEdit"
          color="primary"
          dark
          class="create-btn"
          v-bind="attrs"
          @click="editList"
        >
          Edytuj
        </v-btn>
        <v-btn
          v-else
          color="primary"
          dark
          class="create-btn"
          v-bind="attrs"
          v-on="on"
        >
          Utwórz listę
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="headline">Nazwij swoją listę</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  label="Podaj nazwę listy"
                  required
                  v-model="listName"
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="secondDialog = false">
            Anuluj
          </v-btn>
          <router-link to="Lists">
            <v-btn color="blue darken-1" text @click="createList">
              Zapisz
            </v-btn>
          </router-link>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { mapState } from "vuex";

import Form from "./Form.vue";
import List from "./List.vue";

export default {
  data() {
    return {
      name: "",
      panel: [],
      isVisable: false,
      disableButtons: true,
      dialog: false,
      secondDialog: false,
      index: "",
      listName: "",
      isInEdit: false,
    };
  },
  computed: {
    ...mapState(["list", "requestedListId", "editable"]),

    form() {
      return document.querySelector("form");
    },
  },

  components: {
    Form,
    List,
  },

  methods: {
    all() {
      this.panel = [...Array(this.list.length).keys()].map((k, i) => i);
    },

    none() {
      this.panel = [];
    },

    collappse() {
      this.form.classList.toggle("active");

      if (this.form.classList.contains("active")) {
        this.form.style.maxHeight = this.form.scrollHeight + "px";
      } else {
        this.form.style.maxHeight = 0;
      }

      this.isVisable = !this.isVisable;
    },

    remove(i) {
      this.$store.commit("removeCategory", i);
      this.dialog = false;
    },

    openDialog(i) {
      this.index = i;
      this.dialog = true;
    },

    createList() {
      const data = {
        name: this.listName,
        categories: this.list,
      };

      this.axios.post("http://localhost/api/lists", data, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("access_token")}`,
          "Content-Type": "application/json",
        },
      });

      this.$store.commit("cleanList");

      this.secondDialog = false;
    },

    editList() {
      const data = {
        name: "dsadas",
        is_archived: false,
        categories: this.list,
      };

      this.axios
        .put(`http://localhost/api/lists/${this.requestedListId}`, data, {
          headers: {
            Authorization: `Bearer ${localStorage.getItem("access_token")}`,
            "Content-Type": "application/json",
          },
        })
        .then(() => {
          this.$router.push({ name: "Lists" });
          this.$store.dispatch("changeList", []);
        });
    },
  },

  watch: {
    list() {
      if (this.list.length === 0) {
        this.disableButtons = true;

        this.form.classList.add("active");
        this.form.style.maxHeight = this.form.scrollHeight + "px";
      } else {
        this.disableButtons = false;
      }
    },
  },

  mounted() {
    this.form.style.maxHeight = this.form.scrollHeight + "px";
    if (this.list.length === 0) {
      this.disableButtons = true;

      this.form.classList.add("active");
      this.form.style.maxHeight = this.form.scrollHeight + "px";
    } else {
      this.disableButtons = false;
    }
  },

  created() {
    if (this.editable) {
      this.axios
        .get(`http://localhost/api/lists/${this.requestedListId}`, {
          headers: {
            Authorization: `Bearer ${localStorage.getItem("access_token")}`,
          },
        })
        .then((res) => {
          this.$store.commit("changeList", res.data.categories);
        });

      this.$store.commit("changeEditable", false);
      this.isInEdit = true;
    }
  },
};
</script>


<style lang="scss" scoped>
form {
  transition: max-height 0.4s;
  max-height: 0;
  overflow: hidden;

  &.active {
    overflow: visible;
  }
}

.container {
  position: relative;

  .btn {
    position: absolute;
    right: 0%;
    top: 0%;
  }
}

.white-font {
  color: white !important;
}

.ico {
  display: flex;
  justify-content: flex-end;
  margin-right: 10px;
}

.delete-ico {
  &:hover {
    transform: scale(1.2);
  }
}

.create-btn {
  margin-top: 40px;
  float: right;
  color: white;
}
</style>