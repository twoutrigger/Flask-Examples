from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Name of puppy: ')
    submit = SubmitField('Add puppy')

class OwnerForm(FlaskForm):

    name = StringField('Name of owner: ')
    id = IntegerField('ID of puppy: ')
    submit = SubmitField('Add owner')

class ToyForm(FlaskForm):

    item_name = StringField('Name of toy: ')
    id = IntegerField('ID of puppy: ')
    submit = SubmitField('Add toy')

class DelForm(FlaskForm):

    id = IntegerField('ID number of puppy to remove: ')
    submit = SubmitField('Remove puppy')
