from flask import Flask

def index():
    return '<h1>Стартовая страница</h1>'

def test():
    return '<h1>Здесь будет тест</h1>'

def result():
    return '<h1>Здесь будет результат</h1>'

app = Flask(__name__)
app.add_url_rule('/','index',index)
app.add_url_rule('/test','test',test)
app.add_url_rule('/result','result',result)
app.run()
