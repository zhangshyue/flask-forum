from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_required, login_user, current_user, logout_user
from flaskforum.users.forms import LoginForm, RegisterForm
from flaskforum.replies.forms import ReplyForm
from flaskforum import db, bcrypt
from flaskforum.models import User, Post, Vote, Reply

users = Blueprint('users', __name__)

@users.route("/account", methods=['GET', 'POST'])
def account():
	return render_template('account.html', title = 'Account')

@users.route("/register", methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))
	form = RegisterForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username = form.username.data, email=form.email.data, password = hashed_password)
		db.session.add(user)
		db.session.commit()
		flash('Your account has been created','success')
		return redirect(url_for('users.login'))
	return render_template('register.html', title = 'Register', form =form)

@users.route("/login", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email = form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember = form.remember.data)
			flash('You have been logged in', 'success')
			return redirect(url_for('main.home'))
		else:
			flash('Unsucessful login','danger')
	return render_template('login.html', title = 'Login', form =form)

@users.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('main.home'))

@users.route("/my_posts")
@login_required
def my_posts():
	page = request.args.get('page', 1, type=int)
	posts = Post.query.filter_by(user_id = current_user.id)\
		.order_by(Post.date_posted.desc())\
		.paginate(page=page, per_page=5)
	type = 'post'
	return render_template('my_posts.html', title = 'My Posts', posts = posts
		, type = type)

@users.route("/my_likes")
@login_required
def my_likes():
	page = request.args.get('page', 1, type=int)
	votes = Vote.query.filter_by(user_id = current_user.id, action = 1)
	p = []
	for vote in votes:
		p.append(vote.post_id)
	posts = Post.query.filter(Post.id.in_(p))\
		.order_by(Post.date_posted.desc())\
		.paginate(page=page, per_page=5)
	votes = Vote.query.all()
	form = ReplyForm()
	replies = Reply.query.all()
	return render_template('my_posts.html', title = 'My Likes', posts = posts, 
		type = 'like',votes = votes, form = form, replies = replies)