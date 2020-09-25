<style scoped>

.addmargin {
    margin-top: 10px;
    margin-bottom: 10px;
}

.vue-logo-back {
    background-color: black;
}

</style>

<template>

<div class="home">
    <div class="vue-logo-back">
        <img src="../assets/logo.png" width="100px" height="100px">
    </div>
    <div v-if="taDetails">
        <div class="card" v-if="taDetails.ta">
            <div class="card-header">
                TA Details
            </div>
            <div class="card-body">
                <h5 class="card-title">{{taDetails.ta.name}}</h5>
                <p class="card-text">OH Timings : {{taDetails.ta.time}}</p>
                <a v-on:click="goToMainPage()" class="btn btn-primary"><span style="color:white">Go Back</span></a>
            </div>
        </div>
        <div class="card" v-else-if="taDetails.message">
            <div class="card-header">
                No TA found
            </div>
            <div class="card-body">
                <p class="card-text">{{taDetails.message}}</p>
                <a v-on:click="goToMainPage()" class="btn btn-primary"><span style="color:white">Go Back</span></a>
            </div>
        </div>
    </div>
    <div v-else>Something went wrong</div>


</div>

</template>

<script>

// @ is an alias to /src
import axios from 'axios'

export default {
    name: 'tadetails',
    async mounted() {
        await axios({
            method: "GET",
            "url": "http://flask-env.eba-tzumbnrs.us-east-1.elasticbeanstalk.com/ta/"+this.$route.params.id
        }).then(response => {
            this.taDetails = response.data;
            console.log(this.taDetails)
        }, error => {
            console.error(error);
        });
    },
    data() {
        return {
            taDetails: null
        }
    },
    methods: {
        goToMainPage: function() {
            this.$router.push("/ta");
        }
    }
}

</script>
