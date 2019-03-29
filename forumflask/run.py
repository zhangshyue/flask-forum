
#this module will only run the whole package
from flaskforum import create_app

app = create_app()
#this will start running from the __init__.py file, so app has to be in it
if __name__=='__main__':
	app.run(debug=True)
