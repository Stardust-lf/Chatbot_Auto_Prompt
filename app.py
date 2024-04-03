from flask import Flask, render_template, request, jsonify
from flask import render_template
from core.simplebot import get_answer_with_char
from core.char_prompt import COMPUTER_EXPERT, WRITER

app = Flask(__name__)


# 路由
@app.route('/')
def index():
    #print(chatbot_response('hi'))
    return render_template('dist/index.html')

@app.route('/api/getAnswer', methods=['POST'])
def get_response():

    question = request.json.get('question')

    print('Q',question)
    #response = chatbot_response(question)
    response = get_answer_with_char(question, char_prompt=WRITER, sorce_dir='sources/story.txt')

    print('Ans:', response)
    return jsonify({'answer': response})


# 主程序
if __name__ == "__main__":
    app.run(port=7777)