from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, TextAreaField
from wtforms.validators import DataRequired


class AddProductForm(FlaskForm):
    name = StringField('Name of product', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    image = FileField('Change the image')
    submit = SubmitField('Save')


class AddSupermarketForm(FlaskForm):
    name = StringField('Name of supermarket', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    image = FileField('Change the image')
    submit = SubmitField('Save')
