from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField, SubmitField

class AddForms(FlaskForm):
    name=StringField("What is the name of the puppy?")
    submit = SubmitField("Submit")

class DelForms(FlaskForm):
    id=IntegerField("Enter the id of the puppy you want to remove")
    submit=SubmitField("Submit the option")
