from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, PasswordField, BooleanField, SubmitField, IntegerField, FloatField, SelectField
from wtforms.validators import DataRequired, InputRequired
from wtforms.widgets import TextArea


class TestForm(FlaskForm):
    input_seq = TextAreaField(
        'input_seq', widget=TextArea(), validators=[DataRequired()])
    query_seq = TextAreaField(
        'query_sequence', widget=TextArea(), validators=[DataRequired()])
    target_seq = TextAreaField(
        'target_sequence', widget=TextArea(), validators=[DataRequired()])
    # password = PasswordField('Password', validators=[DataRequired()])
    # remember_me = BooleanField('Remember Me')
    submit = SubmitField('Alginments!')


MASS_CHOICES = [(1.0, 'mg'), (0.001, 'ug'), (0.000001, 'ng')]
VOL_CHOICES = [(1.0, 'ml'), (0.001, 'ul'), (0.000001, 'nl')]


class ConversionForm(FlaskForm):
    molecular_weight = FloatField(validators=[InputRequired()])
    mass = FloatField(validators=[InputRequired()])
    mass_unit = SelectField(choices=MASS_CHOICES, validators=[DataRequired()])
    volume = FloatField(validators=[InputRequired()])
    volume_unit = SelectField(choices=VOL_CHOICES, validators=[DataRequired()])
    submit = SubmitField('Submit!')


class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])


class BufferForm(FlaskForm):
    molecular_weight = FloatField(validators=[InputRequired()])
    molar = FloatField(validators=[InputRequired()])
    molar_unit = SelectField(choices=[(1.0, 'M'), (0.001, 'mM'), (0.000001, 'uM')], validators=[DataRequired()])
    volume = FloatField(validators=[InputRequired()])
    volume_unit = SelectField(choices=[(1000.0, 'L'), (1.0, 'ml'), (0.001, 'ul')], validators=[DataRequired()])
    submit = SubmitField('Submit!')

