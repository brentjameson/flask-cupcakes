from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired

class AddCupcakeForm(FlaskForm):
    """Form for adding pets."""

    flavor = StringField("Flavor", validators = [InputRequired()])

    size = SelectField("Size", choices=[('small', 'small'), ('medium', 'medium'), ('large', 'large')])

    rating = SelectField("Size (1=worst)", choices= [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])

    image = StringField("image", validators = [InputRequired(message= "Enter Valid URL Please.")])
