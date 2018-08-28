import os, random, json
from questions import questions
from flask import Flask, redirect, render_template, request, session, url_for, flash

app = Flask(__name__)
app.secret_key = os.urandom(24)

def ask_question(num):
    return questions[num]['question']


@app.route('/', methods=['GET', 'POST'])
def index():
    pass

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)  