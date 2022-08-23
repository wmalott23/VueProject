<template>
  <v-app>
    <v-main>
      <GetImages/>
    </v-main>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import GetImages from './components/GetImages.vue'

export default {
  name: 'App',

  components: {
    GetImages,
  },

  data: () => ({
    //
  }),
}
</script>
