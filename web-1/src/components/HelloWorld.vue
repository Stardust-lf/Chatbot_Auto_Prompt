<template>
  <div class="common-layout">
    <el-container>
      <el-aside class="aside-with-image" width="200px"></el-aside>
      <el-container>
        <el-header class="header-with-image" >Chatbot Auto Prompt</el-header>
        <el-main>
          <div class="mainContent">
            <el-scrollbar>
              <div class="contentblock"> 
                <div v-for="item in messageList" :key="item.id" class="message">
                  <p class="question">问题: {{ item.message }}</p>
                  <p class="answer">回答: {{ item.answer }}</p>
                </div>
              </div>
            </el-scrollbar>
          </div>
        </el-main>
        <el-footer>
          <el-input v-model="input" style="width: 100%" placeholder="Please input">
              <template #prepend>
                <el-button  @click="clearInput"><i class="custom-icon-clear"></i></el-button>
              </template>
              <template #append>
                <el-button  @click="getInput" ><i class="custom-icon-send"></i></el-button>
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
    clearInput(){
      this.input='';
    },
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
  width: 95%;
  height: 500px;
}
.custom-icon-send {
  background-image: url("cil-send.svg");
  width: 25px;
  background-size: cover;
  background-position: center;
  height: 20px;

}
.custom-icon-clear {
  background-image: url("trash.svg");
  width: 25px;
  background-size: cover;
  background-position: center;
  height: 20px;
}
.aside-with-image {
  background-image: url("undraw_chat_bot_re_e2gj.svg");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: contain;
}
.header-with-image {
  font-weight: bold;
  background-image: url("undraw_chat_re_re1u.svg");
  background-repeat: no-repeat;
  background-position: 20px center;
  background-size: contain;
}

.message {
  display: flex;
  flex-direction: column;
  align-items: flex-end; /* 将消息气泡右对齐 */
  margin-bottom: 10px;
}

.question {
  background-color: #dcf8c6; /* 问题气泡的背景颜色 */
  padding: 10px;
  border-radius: 10px;
  align-self: flex-start; /* 问题气泡左对齐 */
}

.answer {
  background-color: #e5e5ea; /* 回答气泡的背景颜色 */
  padding: 10px;
  border-radius: 10px;
  align-self: flex-end; /* 回答气泡右对齐 */
}
</style>
