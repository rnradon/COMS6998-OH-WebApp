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
    <div class="col-md-6 centeralign">
        <h2>List of TAs</h2>
        
        <div class="card centeralign addmargin" style="width: 18rem;" v-for="ta in talist.ta" :key="ta.id">
            <div class="card-body" v-on:click="setSelectedTa(ta.id)">
                <h5 class="card-title">{{ta.name}}</h5>
                

                <a class="btn btn-primary" v-on:click="goToDetailsPage(ta.id)"><span style="color:white">See schedule</span></a>
            </div>
        </div>
    </div>
    <Display v-if="selectedTa!=''" :selectedTa="selectedTa" />
</div>

</template>

<script>

// @ is an alias to /src
import Display from '@/components/Display.vue'
import axios from 'axios'

export default {
    name: 'ta',
    mounted() {
        axios({
            method: "GET",
            "url": "http://flask-env.eba-tzumbnrs.us-east-1.elasticbeanstalk.com/ta"
        }).then(response => {
            this.talist = response.data;
            console.log(this.talist)
        }, error => {
            // eslint-disable-next-line
            console.error(error);
        });
    },
    data() {
        return {
            talist: [],
            selectedTa: ""
        }
    },
    components: {
        Display
    },
    methods: {
        setSelectedTa: function(name) {
            this.setSelectedTa = name;
        },
        goToDetailsPage: function(id) {
            this.$router.push("/tadetails/"+id);
        }
    }
}

</script>
