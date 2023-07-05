from flask import Flask
import random
import datetime

app = Flask(__name__)

facts_list = [
    'Социальные сети имеют как позитивные, так и негативные стороны, и мы должны быть более осознанными в использовании этих платформ.',
    'Один из способов борьбы с технологической зависимостью - это поиск занятий, которые приносят удовольствие и улучшают настроение.',
    'Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.'

]

a =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

@app.route("/")
def index():
    return '<p1>Привет! Здесь ты можешь узнать пару интересных фактов о технологических зависимостях!</p1>  <a href="/random_fact">Посмотреть случайный факт!</a> <a href="/time">Узнать время!</a>'

@app.route("/random_fact")
def random_facts():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route('/time')
def get_current_time():
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f'<p1>Текущее время: {current_time}</p1>'

app.run(debug=True)