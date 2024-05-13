from flask import render_template, request, jsonify
from app import app
from app.models import *

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # create a new user object
        new_user = User(username=username, email=email, password=password)

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'code': 200, 'message': 'User registered successfully!'})


@app.route('/')
def index():
    # flask for pagination:
    page = request.args.get('page', 1, type=int)
    paginate = Post.query.paginate(page=int(page), per_page=7)
    return render_template('index.html', title='Home', paginate=paginate)

@app.route('/personal-profile')
def personalProfile():
    user = {'username': 'Joel'}
    return render_template('personal-profile.html', title='Profile', user=user)

@app.route('/search')
def search():

    # flask for search paginate:
    page = request.args.get('page', 1, type=int)
    search_keywords = request.args.get('search_keywords')

    paginate = Post.query.filter(Post.body.contains(search_keywords)).paginate(page=page, per_page=7)

    return render_template('index.html', title='Home', paginate=paginate)
    
@app.route('/new-discussion')
def newDiscussion():
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
    