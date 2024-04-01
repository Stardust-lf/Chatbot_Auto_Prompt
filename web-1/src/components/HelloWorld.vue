<template>
  <div class="common-layout">
    <el-container>
      <el-aside width="200px">Aside</el-aside>
      <el-container>
        <el-header>Header</el-header>
        <el-main>
          <div class="mainContent">
            <el-scrollbar>
              <div class="contentblock"> 
                <div v-for="item in messageList" :key="item.id">
                  <p>问题: {{ item.message }}</p>
                  <p>回答: {{ item.answer }}</p>
                </div>
              </div>
            </el-scrollbar>
          </div>
        </el-main>
        <el-footer>
          <el-input v-model="input" style="width: 100%" placeholder="Please input">
              <template #prepend>
                <el-button :icon="Search" @click="getInput" />
              </template>
              <template #append>
                <el-button :icon="Search" @click="getInput" />
              </template>
            </el-input>
          </el-footer>
      </el-container>
    </el-container>
  </div>
</template>

<script>
// import { ref } from 'vue'
import axios from 'axios';

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return{
      input: 'hhhh',
      messageList: [],
    }
  },
  methods:{
    async getInput() {
      try {
        const response = await axios.post('/api/getAnswer', { question: this.input });
        // 假设回答在response.data.answer中
        this.messageList.push({
          id: this.messageList.length + 1,
          message: this.input,
          answer: response.data.answer
        });
        // 清空输入框以便下一次输入
        this.input = '';
      } catch (error) {
        console.error('API调用失败', error);
        // 处理错误，例如显示错误消息
      }
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
