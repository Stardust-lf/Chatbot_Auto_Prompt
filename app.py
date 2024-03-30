from flask import Flask
from flask import render_template
from core.chatbot import chatbot_response

app = Flask(__name__)



@app.route('/')
def index():
    #print(chatbot_response('hi'))
    return render_template('dist/index.html')


if __name__ == "__main__":
    app.run(port=7777)