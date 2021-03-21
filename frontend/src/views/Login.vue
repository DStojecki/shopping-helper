<template>
    <div class="wrapper">
        <div class="bgc">
            <div class="panel">
                <form>
                    <v-text-field
                    label="Login użytkownika"
                    required
                    v-model="login"
                    :error-messages="loginErrors"
                    @input="$v.login.$touch()"
                    @blur="$v.login.$touch()"
                    ></v-text-field>
                    <v-text-field
                    type="password"
                    v-model="password"
                    :error-messages="nameErrors"
                    label="Password"
                    required
                    @input="$v.password.$touch()"
                    @blur="$v.password.$touch()"
                    ></v-text-field>
                    <v-btn
                    class="mr-4 mt-6"
                    @click="submit"
                    >
                    Login
                    </v-btn>
                    <Register />
                </form>
            </div>
        </div>
    </div>
</template>


<script>
  import { validationMixin } from 'vuelidate'
  import { required, minLength } from 'vuelidate/lib/validators'
  import Register from '../components/Register.vue'

  export default {
    mixins: [validationMixin],

    validations: {
      password: { required },
     login: {required, minLength: minLength(6)}
    },

    data: () => ({
      password: '',
      login: '',
    }),

    components: {
        Register,
    },

    computed: {
      nameErrors () {
        const errors = []
        if (!this.$v.password.$dirty) return errors
        !this.$v.password.required && errors.push('Hasło jest wymagane.')
        return errors
      },loginErrors () {
        const errors = []
        if (!this.$v.login.$dirty) return errors
        !this.$v.login.required && errors.push('Login jest wymagany.')
        !this.$v.login.minLength && errors.push('Login powinien mieć minimum 6 znaków')
        return errors
      },
    },

    methods: {
      submit () {
        this.$v.$touch()
        this.$store.commit("changeIsLogged", true)
        const data = {
                username: this.login,
                password: this.password
        }

            this.axios.post("http://localhost/api/auth/token", data).then((response) => {
            console.log(response)
        })
      },
    },
  }
</script>



<style lang="scss" scoped>
    .wrapper {
        background: url(../../public/img/background.jpg);
        background-repeat: no-repeat;
        background-size: cover;
    }

    .bgc {
        width: 100vw;
        height: 100vh;
        background-color: rgba(106, 118, 171, 0.67);
        border: rgba(106, 118, 171, 0.67);
        position: relative;
    }

    .panel {
        width: 500px;
        border-radius: 4px;
        background-color: white;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        padding: 20px 30px;
    }
</style>