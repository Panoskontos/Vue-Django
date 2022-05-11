<template>
  <div class="container">
    <h2>Tasks</h2>

    <input type="text" v-model="taskName" @keyup.enter="createObject" >


     <ul>
      <!-- animation -->
      <transition-group enter-active-class="animate__animated animate__backInUp" leave-active-class="animate__animated animate__backOutLeft">
      
      <li v-for="task of tasks" :key="task.id">
      
      <div class="normal-mode">
          
          {{task.name}} 

           <!-- <i v-on:click="showEdit(task.id)" class="bi bi-pencil"></i> --> 
           <i v-on:click="deleteObject(task.id)" class="bi bi-trash2"></i>
      </div>
      
      <!-- <div class="edit-mode invisible">
          <input type="text" v-model="editName" @keyup.enter="editObject(task.id)">
      </div> -->
      
      </li>
      
      </transition-group>
    
    </ul>
  </div>
</template>

<script>

import axios from 'axios';

const baseURL = 'http://localhost:3000/api/tasks/'
export default {

  name: 'App',
  data(){
    return {
      tasks: [],
      taskName:'',
      taskFinished: false,
    }
  },

  components: {},
  
  async created(){
    try {
      const res = await axios.get(baseURL);
      console.log(res.data)
      this.tasks = res.data;
    } catch(e) {
      console.error(e)
    }
  },

  methods: {
    // CREATE
    async createObject(){
      // post request
      const res = await axios.post(baseURL, {name: this.taskName, finished:this.taskFinished});
      console.log(res)
      // concatinate in our data
      this.tasks.push(res.data)
      this.taskName = ''
    },

    // DELETE
    async deleteObject(id){
      const res = await axios.delete(baseURL + id);
      this.tasks = this.tasks.filter( function(el) { return el.id != id})

    },
   
    

  }


}
</script>

<style>
body {
background: #83a4d4;  /* fallback for old browsers */
background: -webkit-linear-gradient(to right, #b6fbff, #83a4d4);  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to right, #b6fbff, #83a4d4); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

}

#app {
  
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.container {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  background-color: white;
  border-radius: 10px;
  position: absolute;
  width: 400px;
  left: 20vw;
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
}

ul {
      padding-inline-start: 0px;
}

li {
  list-style: none;
  /* background-color: blueviolet; */
background: #8E2DE2;  /* fallback for old browsers */
background: -webkit-linear-gradient(to right, #4A00E0, #8E2DE2);  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to right, #4A00E0, #8E2DE2); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

  width: 200px;
  color: white;
  margin: 10px;
  padding: 5px;
  border-radius: 10px;
  text-align: center;
  position: relative;
}

input[text] {
  width:200px;
  padding:5px;
  border-radius:15px;
  border:1px solid rgb(231, 231, 231);
  box-shadow:4px 4px 10px rgba(0,0,0,0.06);
}

.normal-mode {
  position: relative;
}

.check {
  position: absolute;
  left: 0;
}

.invisible {
  display: none;
}


.bi-trash2 {
  position: absolute;
  right: 10px;
  cursor: pointer;
}
.bi-pencil {
  position: absolute;
  left: 15px;
  cursor: pointer;
}
.edit-mode input{
  background-color: blueviolet;
  color: white;
}
</style>
