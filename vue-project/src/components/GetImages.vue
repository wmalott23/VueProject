<template>
    <v-container
        style="max-height: 50px"
    >
        <v-card v-for="image in images"
            style="height: 50px"
            outlined
            tiled
        >
            <img :src="image.image_url">
        </v-card>
    </v-container>
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
.img {
    width: 50%;
}

</style>