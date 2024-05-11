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
   
def question_form(question):
   answers_list = [question[2],question[3],question[4],question[5]]
   shuffle(answers_list)
   return render_template('test.html',question=question[1],quest_id=question[0],answers_list=answers_list)



def test():
   if not ('quiz' in session) or int(session['quiz']) < 0:
      return redirect(url_for('index'))
   else:
      if request.method == 'POST':
         pass
         #save_answers()
      next_question = get_question_after(session['last_question'], session['quiz'])
      if next_question is None or len(next_question) == 0:
         return redirect(url_for('result'))
      else:
         return question_form(next_question)






def result():
   return "that's all folks!"

folder = os.getcwd()
# Создаём объект веб-приложения:
app = Flask(__name__,template_folder=folder,static_folder=folder) 
app.add_url_rule('/', 'index', index, methods=['post','get'])   # создаёт правило для URL '/'
app.add_url_rule('/test', 'test', test, methods=['post','get']) # создаёт правило для URL '/test'
app.add_url_rule('/result', 'result', result) # создаёт правило для URL '/test'
# Устанавливаем ключ шифрования:
app.config['SECRET_KEY'] = 'ThisIsSecretSecretSecretLife'

if __name__ == '__main__':
   # Запускаем веб-сервер:
   app.run()
