from flask import render_template, request, jsonify, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy import desc
from app import app
from app.models import *
from sqlalchemy import or_
from concurrent.futures import ThreadPoolExecutor



@app.route('/register', methods=['POST'])
def register():
    # this route can only be accessed by POST method
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
        # retrieve the username and password from the request
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            return jsonify({'code': 201, 'message': 'Invalid input!'})

        # find the user by username
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
    page = request.args.get('page', 1, type=int)
    # get the category id from the query string
    category_id = request.args.get('category')
    if category_id:
        # filter the posts by category id
        paginate = Post.query.filter_by(category_id=category_id).paginate(page=page, per_page=7)
    else:
        # get all posts
        paginate = Post.query.paginate(page=page, per_page=7)

    # get all categories
    categories = Category.query.all()

    return render_template('index.html', user=current_user, categories=categories, paginate=paginate)


@app.route('/personal-profile', methods=['GET', 'POST'])
def personalProfile():
    # This function can be accessed by both GET and POST methods
    # GET method: display the personal profile page
    # POST method: update the user's bio
    user = current_user
    posts = Post.query.filter_by(author_id=user.id).all()

    if request.method == 'POST':
        new_bio = request.form.get('new_bio')
        # update the database
        user.bio = new_bio
        db.session.commit()
        # redirect to the personal profile page
        return redirect(url_for('personalProfile'))

    return render_template('personal-profile.html', title='Personal Profile', user=user, posts=posts)

@app.route('/user-posts/<username>')
def user_posts(username):
    # Find the user by username
    user = User.query.filter_by(username=username).first_or_404()

    # Retrieve all posts by the user
    user_posts = Post.query.filter_by(author=user).all()

    return render_template('user_posts.html', user=user, user_posts=user_posts)


@app.route('/search')
def search():
    # flask for search paginate:
    page = request.args.get('page', 1, type=int)
    search_keywords = request.args.get('search_keywords')

    paginate = Post.query.filter(or_(Post.title.contains(search_keywords), Post.body.contains(search_keywords))).paginate(page=page, per_page=7)


    return render_template('index.html', title='Home', paginate=paginate)


@app.route('/new-discussion', methods=['GET', 'POST'])
def newDiscussion():
    # This function can be accessed by both GET and POST methods
    # GET method: display the new discussion page
    # POST method: create a new post
    if request.method == 'GET':
        if not current_user.is_authenticated:
            return jsonify({'code': 201, 'message': 'Please login first!'})
        categories = Category.query.all()
        return render_template('new-discussion.html', categories=categories, user=current_user)

    elif request.method == 'POST':
        if not current_user.is_authenticated:
            return jsonify({'code': 201, 'message': 'Please login first!'})

        category_id = request.form['category_id']
        title = request.form['title']
        body = request.form['body']

        author_id = current_user.id

        new_post = Post(body=body, author_id=author_id, category_id=category_id, title=title)
        db.session.add(new_post)
        db.session.commit()

        current_user.credit += 5
        db.session.commit()

        return jsonify({'code': 200, 'post_id': new_post.id})


def robohash_url(text):
    # generate a random avatar based on the text
    return f"https://robohash.org/{text}"


@app.route('/ranking-page')
def rankingPage():
    users = User.query.order_by(desc(User.credit)).all()
    for user in users:
        user.robohash_url = robohash_url(user.email)
    return render_template("ranking-page.html", title='Ranking page', users=users)
 
@app.route('/post-details/<int:post_id>', methods=['GET', 'POST'])
def postDetails(post_id):

    if request.method == 'GET':
        post = Post.query.get_or_404(post_id)
        comments = Comment.query.filter_by(post_id=post_id).all()
        return render_template("post-details.html", title='Post details', post=post, comments=comments, user=current_user)
    
    if request.method == 'POST':
        if not current_user.is_authenticated:
            return jsonify({'code': 201, 'message': 'Please login first!'})
      
        body = request.form['body']
        author_id = current_user.id

        new_comment = Comment(body=body, author_id=author_id, post_id=post_id)
        db.session.add(new_comment)

        current_user.credit += 1
        db.session.commit()

        # create a new thread to generate gpt-3.5 response

        return jsonify({'code': 200, 'comment_id': new_comment.id})
    
    
