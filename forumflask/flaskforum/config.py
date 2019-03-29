import os

class Config:
	#for best practice, we should put secret_key and database_uri
	#in environment variables to hide these info
	SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' 
	#set up gmail
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 587
	MAIL_USER_TLS = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False