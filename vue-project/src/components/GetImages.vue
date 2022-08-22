<template>
  <ul>
    <li v-for="image in images">
      <h3>
          {{image.title}}
      </h3>
      <button>
        X
      </button>
    </li>
  </ul>
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