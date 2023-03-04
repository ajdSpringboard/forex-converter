from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import InputRequired

class CurrencyForm(FlaskForm):
    curr_from = StringField('Currency From: ', validators=[InputRequired()])
    curr_to = StringField('Currency To: ', validators=[InputRequired()])
    curr_amt = DecimalField('Amount: ', validators=[InputRequired()])
    submit = SubmitField('Submit')