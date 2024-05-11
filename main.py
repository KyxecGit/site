import os
from random import shuffle
from flask import Flask, session, redirect, url_for, render_template, request
from db import get_question_after, get_quises, check_answer

def start_quiz(quiz_id):
   session['quiz'] = quiz_id
   session['last_question'] = 0
   session['answers'] = 0
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
   else:
      quest_id = request.form.get('quiz')
      start_quiz(quest_id)
      return redirect(url_for('test'))

def test():
   result = get_question_after(session['last_question'], session['quiz'])
   if result is None or len(result) == 0:
       return redirect(url_for('result'))
   else:
       session['last_question'] = result[0]
       # если мы научили базу возвращать Row или dict, то надо писать не result[0], а result['id']
       return '<h1>' + str(session['quiz']) + '<br>' + str(result) + '</h1>'

def result():
   return "that's all folks!"

folder = os.getcwd()
# Создаём объект веб-приложения:
app = Flask(__name__,template_folder=folder,static_folder=folder) 
app.add_url_rule('/', 'index', index, methods=['post','get'])   # создаёт правило для URL '/'
app.add_url_rule('/test', 'test', test) # создаёт правило для URL '/test'
app.add_url_rule('/result', 'result', result) # создаёт правило для URL '/test'
# Устанавливаем ключ шифрования:
app.config['SECRET_KEY'] = 'ThisIsSecretSecretSecretLife'

if __name__ == '__main__':
   # Запускаем веб-сервер:
   app.run()
