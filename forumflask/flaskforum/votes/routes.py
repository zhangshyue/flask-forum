from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_required, login_user, current_user, logout_user
from flaskforum import db
from flaskforum.models import User, Post, Vote

votes = Blueprint('votes', __name__)

@votes.route("/<int:user_id>/<int:post_id>/upvote", methods = ['POST'])
@login_required
def upvote(user_id, post_id):
	vote = Vote.query.filter_by(user_id = user_id, post_id = post_id, action = 1).first()
	down = Vote.query.filter_by(user_id = user_id, post_id = post_id, action = -1).first()
	if vote:
		db.session.delete(vote)
		db.session.commit()
	if not vote:
		post = Post.query.get_or_404(post_id)
		vote = Vote(action = 1, user = current_user, post = post)
		if down:
			db.session.delete(down)
		db.session.add(vote)
		db.session.commit()
		flash('You have successfully voted!', 'success')
	return redirect(url_for('main.home'))

@votes.route("/<int:user_id>/<int:post_id>/downvote", methods = ['POST'])
@login_required
def downvote(user_id, post_id):
	vote = Vote.query.filter_by(user_id = user_id, post_id = post_id, action = -1).first()
	up = Vote.query.filter_by(user_id = user_id, post_id = post_id, action = 1).first()
	if vote:
		db.session.delete(vote)
		db.session.commit()
	if not vote:
		post = Post.query.get_or_404(post_id)
		vote = Vote(action = -1, user = current_user, post = post)
		if up:
			db.session.delete(up)
		db.session.add(vote)
		db.session.commit()
		flash('You have successfully voted!', 'success')
	return redirect(url_for('main.home'))