from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flaskforum.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
#this 'login' means url_for('login'), this line if for login_required
login_manager.login_message_category = 'info'
#this line is to change the style according to bootstrap style


#good practice to put extensions here
def create_app(config_class = Config):
	app = Flask(__name__)
	app.config.from_object(Config)
	app.app_context().push()
	db.init_app(app)
	bcrypt.init_app(app)
	login_manager.init_app(app)
	#we are importing blueprint here
	from flaskforum.users.routes import users
	from flaskforum.posts.routes import posts
	from flaskforum.main.routes import main
	from flaskforum.votes.routes import votes
	from flaskforum.replies.routes import replies
	# from flaskblog.errors.handlers import errors
	app.register_blueprint(users)
	app.register_blueprint(posts)
	app.register_blueprint(main)
	app.register_blueprint(votes)
	app.register_blueprint(replies)
	# app.register_blueprint(errors)
	return app
