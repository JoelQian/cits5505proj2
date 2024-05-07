from flask import render_template, request
from app import app
from app.models import Post


@app.route('/')


@app.route('/index')

def index():

    # flask for pagination:

    page = request.args.get('page', 1, type=int)

    paginate = Post.query.paginate(page=int(page), per_page=7)

    return render_template('index.html', title='Home', paginate=paginate)

    # template for posts(including the variable names used in HTML):
    # posts = [
    #     {
    #         'posttitle': 'Welcome to Portland',
    #         'author': {'username': 'David', 'avatar': 'https://placehold.co/50'},
    #         'body': 'Beautiful day in Portland!',
    #         'tag': 'Support',
    #         'comment_count': '5'
    #     },
    #     {
    #         'posttitle': 'I love Avengers',
    #         'author': {'username': 'Joel', 'avatar': 'https://placehold.co/50'},
    #         'body': 'The Avengers movie was so cool!',
    #         'tag': 'Extensions',
    #         'comment_count': '10'
    #     }
    # ]
    # return render_template('index.html', title='Home', posts=posts)

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
    
    # template for search posts(including the variable names used in HTML):
    # posts = [
    #     {
    #         'posttitle': 'Search Results for ' + search_keywords,
    #         'author': {'username': 'David', 'avatar': 'https://placehold.co/50'},
    #         'body': 'Beautiful day in Portland!',
    #         'tag': 'Support',
    #         'comment_count': '5'
    #     }
    # ]
    # return render_template('index.html', title='Search Results', posts=posts)