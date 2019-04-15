from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class EntryForm(FlaskForm):

    area = SelectField(u'Which district would you like to eat in?',
                        choices=[('e','Eastern'),('ec','Eastern Central'),('n','Northern'),
                                 ('nw','North Western'),('se','South Eastern'),('sw','South Western'),
                                 ('w','Western'),('wc','Western Central')],
                        validators=[DataRequired()])

    cuisine = SelectField(u'What cuisine would you interested in?',
                          choices=[('greek','Greek'),('indian','Indian'),('italian','Italian'),
                                   ('japanese','Japanese'),('american','American')],
                          validators=[DataRequired()])

    diningtime = SelectField(u'When would you want to eat?',
                             choices=[('breakfast','Breakfast'),('lunch','Lunch'),('dinner','Dinner'),
                             ('anytime','Anytime')],
                             validators=[DataRequired()])

    submit = SubmitField('Submit')


class HashForm(FlaskForm):

    password_input = StringField('Enter a password to be hashed: ', validators=[DataRequired()])

    hash_type = SelectField(u'What hash type would you like? ',
                        choices=[('MD5','MD5'),('SHA-1','SHA-1'),('SHA-256','SHA-256'),('SHA-512','SHA-512')],
                        validators=[DataRequired()])

    submit = SubmitField('Submit')
