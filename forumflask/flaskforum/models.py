from datetime import datetime
from flaskforum import db, login_manager
from flask import current_app
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	__tablename__='user'
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(20), unique=True, nullable = False)
	email = db.Column(db.String(120), unique=True, nullable = False)
	image_file = db.Column(db.String(20), nullable = False, default='default.jpg')
	password = db.Column(db.String(60), nullable = False)
	posts = db.relationship('Post', backref = 'author', lazy = True)
	votes = db.relationship('Vote', backref = 'user', lazy = True)
	replies = db.relationship('Reply', backref = 'user', lazy = True)

	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.password}')"

class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(100), nullable = False)
	date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
	content = db.Column(db.Text, nullable = False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
	replies = db.relationship('Reply', backref = 'post', lazy = True)
	votes = db.relationship('Vote', backref = 'post', lazy = True)

	def __repr__(self):
		return f"Post('{self.title}', '{self.date_posted}')"

class Vote(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
	post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable = False)
	action = db.Column(db.Integer, nullable=False)
	date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

	def __repr__(self):
		return f"Vote('{self.action}')"

class Reply(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
	content = db.Column(db.Text, nullable = False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
	post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable = False)
	def __repr__(self):
		return f"Reply('{self.content}')"