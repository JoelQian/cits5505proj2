from flask import render_template, request, jsonify, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from app import app
from app.models import *


@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # create a new user object
        new_user = User(username=username, email=email)
        new_user.set_password(password)

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'code': 200, 'message': 'User registered successfully!'})
    return jsonify({'code': 400, 'message': 'Bad request!'})


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            return jsonify({'code': 201, 'message': 'Invalid input!'})

        user = User.query.filter_by(username=username).first()

        if not user or not user.validate_password(password):
            return jsonify({'code': 202, 'message': 'Invalid username or password!'})

        login_user(user)
        return jsonify({'code': 200, 'message': 'Login successful!'})
    return jsonify({'code': 400, 'message': 'Bad request!'})


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/')
def index():
    # flask for pagination:
    page = request.args.get('page', 1, type=int)
    paginate = Post.query.paginate(page=int(page), per_page=7)
    categories = Category.query.all()

    return render_template('index.html', user=current_user, categories=categories, paginate=paginate)


@app.route('/personal-profile')
def personalProfile():
    user = {'username': 'Joel'}
    return render_template('personal-profile.html', title='Profile', user=user)


@app.route('/search')
def search():

    # flask for search paginate:
    page = request.args.get('page', 1, type=int)
    search_keywords = request.args.get('search_keywords')

    paginate = Post.query.filter(Post.body.contains(
        search_keywords)).paginate(page=page, per_page=7)

    return render_template('index.html', title='Home', paginate=paginate)


@app.route('/new-discussion')
def newDiscussion():
    if request.method == 'GET':
        if not current_user.is_authenticated:
            return jsonify({'code': 201, 'message': 'Please login first!'})

    # for 'GET' method, we need {{user.avatar}} to display the user's avatar
    user = [
        {
            'avatar': 'https://placehold.co/50'
        }
    ]
    return render_template('new-discussion.html', title='New Discussion', user=user)
    # for 'POST' method, the 'name' attributes in the HTML submit form are:
    #   'tag' - for user input of discussion tags
    #   'title' - for user input of discussion title
    #   'editor' - for user input of discussion content


@app.route('/ranking-page')
def rankingPage():
    return render_template("ranking-page.html")
