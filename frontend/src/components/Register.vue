<template>
    <v-dialog
      v-model="dialog"
      persistent
      max-width="600px"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color=""
          v-bind="attrs"
          v-on="on"
          class="mt-6 mr-4"
        >
          Rejestracja
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="headline">User Profile</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  label="Email*"
                  required
                  v-model="email"
                  :error-messages="emailErrors"
                  @input="$v.email.$touch()"
                  @blur="$v.email.$touch()"
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  label="Login użytkownika*"
                  required
                  v-model="login"
                  :error-messages="loginErrors"
                  @input="$v.login.$touch()"
                  @blur="$v.login.$touch()"
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  label="Hasło*"
                  type="password"
                  required
                  v-model="password"
                  :error-messages="passwordErrors"
                  @input="$v.password.$touch()"
                  @blur="$v.password.$touch()"
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  label="Powtórz hasło*"
                  type="password"
                  required
                  v-model="repeatPassword"
                  :error-messages="repeatPasswordErrors"
                  @input="$v.repeatPassword.$touch()"
                  @blur="$v.repeatPassword.$touch()"
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
          <small>* pola wymagane</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            @click="dialog = false"
          >
            Anuluj
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            @click="submit"
            :disabled="$v.$invalid"
        
          >
            Potwierdź
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
</template>


<script>
import { validationMixin } from 'vuelidate'
import { required, email, minLength, sameAs } from 'vuelidate/lib/validators'

  export default {
    data: () => ({
      dialog: false,
      email: "",
      login: "",
      password: "",
      repeatPassword: "",
    }),

    mixins: [validationMixin],

    validations: {
      password: { required, minLength: minLength(6)},
      repeatPassword: { sameAsPassword: sameAs('password')},
      email: { required, email },
      login: {required, minLength: minLength(6)}
    },

    computed: { 
      passwordErrors () {
        const errors = []
        if (!this.$v.password.$dirty) return errors
        !this.$v.password.required && errors.push('Hasło jest wymagane.')
        !this.$v.password.minLength && errors.push('Hasło powinno mieć minimum 6 znaków')
        return errors
      },
      repeatPasswordErrors () {
        const errors = []
        if (!this.$v.repeatPassword.$dirty) return errors
        !this.$v.repeatPassword.sameAsPassword && errors.push('Hasła nie są identyczne.')
        return errors
      },emailErrors () {
        const errors = []
        if (!this.$v.email.$dirty) return errors
        !this.$v.email.email && errors.push('Nieprawidłowy email')
        !this.$v.email.required && errors.push('Email jest wymagany')
        return errors
      },
      loginErrors () {
        const errors = []
        if (!this.$v.login.$dirty) return errors
        !this.$v.login.required && errors.push('Login jest wymagany.')
        !this.$v.login.minLength && errors.push('Login powinien mieć minimum 6 znaków')
        return errors
      },
    },

    methods: {
        submit() {
            const data = {
                email: this.email,
                username: this.login,
                password: this.password
            }

            this.axios.post("http://localhost/api/auth/register", data)
            
            this.dialog = false
            this.email = ""
            this.username = ""
            this.password = ""
            }
        }
    }
  
</script>