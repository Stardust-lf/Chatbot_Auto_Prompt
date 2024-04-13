from flask import Flask, render_template, request, jsonify
from flask import render_template
from core.utils import get_char
from core.simplebot import get_answer_with_char
from core.char_prompt import COMPUTER_EXPERT, WRITER, RESOURCE_FINDER
import sys
import os

app = Flask(__name__)
CHAR_DICT = ''
KEY = 'xxx'
if len(sys.argv) == 1:
    print('Please provide the OPENAI-KEY')
    sys.exit()
else:
    print('Running on key:', sys.argv[1])
    os.environ["OPENAI_API_KEY"] = sys.argv[1]


@app.route('/')
def index():
    return render_template('dist/index.html')


@app.route('/api/getAnswer', methods=['POST'])
def get_response():
    question = request.json.get('question')
    char_prompt_para = request.json.get('optionsPara')
    #CHAR_DICT = get_answer_with_char(question, char_prompt=RESOURCE_FINDER, sorce_dir = 'sources/self.txt')
    resource_response = get_char(question)
    print('S', resource_response)
    print('role', char_prompt_para)
    # response = chatbot_response(question)
    response = ''
    if char_prompt_para == "WRITER":
        response = get_answer_with_char(question, char_prompt=WRITER, sorce_dir='sources/{}.txt'.format(resource_response))
    elif char_prompt_para == "COMPUTER_EXPERT":
        response = get_answer_with_char(question, char_prompt=COMPUTER_EXPERT, sorce_dir='sources/self.txt')

    print('Ans:', response)
    return jsonify({'answer': response})


# 主程序
if __name__ == "__main__":
    app.run(port=7777)
