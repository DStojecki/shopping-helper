<template>
  <div class="home">
    <Builder />
  </div>
</template>

<script>
// @ is an alias to /src
import Builder from '@/components/Builder.vue'

export default {
  name: 'Home',
  components: {
    Builder
  }
}
</script>


<style lang="scss" scoped>
    .home {
        padding: 30px;
    }

    @media(max-width: 500px) {
        .home {
            padding: 5px;
        }
    }
</style>