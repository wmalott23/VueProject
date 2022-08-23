<template>
    <div v-for="image in images">
          <img :src="image.image_url">
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: "get-images",
    data() {
        return {
            images: null
        }
    },
    async created() {
        const response = await axios.get("http://127.0.0.1:8000/api/images/")
        this.images = response.data
        console.log(this.images)
    },
}
</script>

<style>

div {
  display: block;
  max-width: 100px;
  max-height: 100px;
  padding: 10px;
  margin: 10px
}

</style>