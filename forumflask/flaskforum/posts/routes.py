from flask import render_template, redirect, flash, request, abort, Blueprint, url_for
from flask_login import current_user, login_required
from flaskforum import db
from flaskforum.models import Post
from flaskforum.posts.forms import PostForm

posts = Blueprint('posts', __name__)

@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
	form= PostForm()
	if form.validate_on_submit():
		post = Post(title=form.title.data, content = form.content.data, author = current_user)
		db.session.add(post)
		db.session.commit()
		flash('Your post has been created', 'success')
		return redirect(url_for('main.home'))
	return render_template('create_post.html', title = 'New Post',
		form = form, legend = 'New Post', action = 'Create')

@posts.route("/post/<int:post_id>/update", methods = ['GET','POST'])
@login_required
def update_post(post_id):
	post = Post.query.get_or_404(post_id)
	form = PostForm()
	if form.validate_on_submit():
		post.title = form.title.data
		post.content = form.content.data
		db.session.commit()
		flash('Your post has been updated', 'success')
		return redirect(url_for('users.my_posts'))
	elif request.method == 'GET':
		form.title.data = post.title
		form.content.data = post.content
	return render_template('create_post.html', title = 'Update Post',
		form = form, legend = 'New Post', action = 'Update')

@posts.route("/post/<int:post_id>/delete", methods = ['POST'])
@login_required
def delete_post(post_id):
	post = Post.query.get_or_404(post_id)
	db.session.delete(post)
	db.session.commit()
	flash('Your post has been deleted', 'info')
	return redirect(url_for('users.my_posts'))