import os
from random import shuffle
from flask import Flask , session, request , redirect, render_template, url_for
from db import get_question_after, get_quises, check_answer

def start_quiz(quiz_id):
    session['quiz'] = quiz_id
    session['last_question'] = 0
    session['answer'] = 0
    session['total'] = 0

def end_quiz():
    session.clear()

def quiz_form():
    q_list = get_quises()
    return render_template('index.html', q_list = q_list)

def index():
    if request.method == 'GET':
        start_quiz(-1)
        return quiz_form()

def test():
    return '<h1>Здесь будет тест</h1>'

def result():
    return '<h1>Здесь будет результат</h1>'

folder = os.getcwd()

app = Flask(__name__,template_folder=folder,static_folder=folder)

app.add_url_rule('/','index',index, methods=['post','get'])
app.add_url_rule('/test','test',test, methods=['post','get'])
app.add_url_rule('/result','result',result)

app.config['SECRET_KEY'] = 'QWERTYUIOPOIUYTREWERTYUIOOIU'

app.run()
