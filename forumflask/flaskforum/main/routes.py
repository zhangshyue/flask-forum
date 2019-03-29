from flask import render_template, request, Blueprint
from flaskforum.models import Post, Vote, Reply, User
from flask_login import current_user, login_required
from flaskforum.replies.forms import ReplyForm

main = Blueprint('main',__name__)

@main.route("/")
@main.route("/home")
def home():
	page = request.args.get('page', 1, type=int)
	posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
	votes = Vote.query.all()
	form = ReplyForm()
	replies = Reply.query.all()
	return render_template('home.html', title = 'Home', 
		posts = posts, votes = votes, form = form, replies = replies)


# @main.route("/home")
# @login_required
# def home_login():
# 	page = request.args.get('page', 1, type=int)
# 	posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
# 	votes = Vote.query.all()
# 	form = ReplyForm()
# 	replies = Reply.query.all()
# 	return render_template('home.html', title = 'Home', 
# 		posts = posts, votes = votes, form = form, replies = replies)