<template>
  <div class="common-layout">
    <el-container>
      <el-header>Header</el-header>
      <el-container>
        <el-aside width="200px">Aside</el-aside>
        <el-main>
          <div class="mainContent">
            <div class="contentblock"> 

            </div>
            <el-input v-model="input" style="width: 100%" placeholder="Please input">
              <template #prepend>
                <el-button :icon="Search" @click="getInput" />
              </template>
              <template #append>
                <el-button :icon="Search" @click="getInput" />
              </template>
            </el-input>
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
// import { ref } from 'vue'
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return{
      input: 'hhhh',
    }
  },
  methods:{
    getInput(){
      console.log(this.input)
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.mainContent{
  display: flex;
  flex-direction: column;
  background-color: #FAFAFA;
  width: 100%;
  height: 100%;
}
.contentblock{
  width:500px;
  height: 500px;
}
</style>
