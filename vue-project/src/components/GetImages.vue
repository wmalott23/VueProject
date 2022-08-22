<template>
    <div>
        <h5>
            {{images}}
        </h5>
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
        this.images = response.data.total
    },
}
</script>