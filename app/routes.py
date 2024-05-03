from flask import render_template
from app import app

@app.route('/')


@app.route('/index')
def index():
    posts = [
        {
            'posttitle': 'Welcome to Portland',
            'author': {'username': 'David'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'posttitle': 'I love Avengers',
            'author': {'username': 'Joel'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)

@app.route('/personal-profile')
def personalProfile():
    user = {'username': 'Joel'}
    return render_template('personal-profile.html', title='Profile', user=user)