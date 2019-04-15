from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
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
