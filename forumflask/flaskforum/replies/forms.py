from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ReplyForm(FlaskForm):
	content = TextAreaField('Content', validators = [DataRequired()])
	submit = SubmitField('Reply')