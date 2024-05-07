import os
from random import shuffle
from flask import Flask , session, request , redirect, render_template, url_for
from db import get_question_after, get_quises, check_answer

def index():
    return '<h1>Стартовая страница</h1>'

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
