from flask import Flask, render_template, request, jsonify
from flask import render_template
from core.simplebot import get_answer_with_char
from core.char_prompt import COMPUTER_EXPERT, WRITER
import sys
import os

app = Flask(__name__)
KEY = 'xxx'
if len(sys.argv) == 1:
    print('Please provide the OPENAI-KEY')
    sys.exit()
else:
    print('Running on key:',sys.argv[1])
    os.environ["OPENAI_API_KEY"] = sys.argv[1]

# 路由
@app.route('/')
def index():
    #print(chatbot_response('hi'))
    return render_template('dist/index.html')

@app.route('/api/getAnswer', methods=['POST'])
def get_response():

    question = request.json.get('question')
    char_prompt_para = request.json.get('optionsPara')

    print('Q',question)
    print('role',char_prompt_para)
    #response = chatbot_response(question)
    response = ''
    if char_prompt_para == "COMPUTER_EXPERT":
        response = get_answer_with_char(question, char_prompt=COMPUTER_EXPERT, sorce_dir='sources/story.txt', )
    elif char_prompt_para == "WRITER":
        response = get_answer_with_char(question, char_prompt=WRITER, sorce_dir='sources/story.txt', )

    print('Ans:', response)
    return jsonify({'answer': response})


# 主程序
if __name__ == "__main__":
    app.run(port=7777)