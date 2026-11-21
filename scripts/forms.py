from flask_wtf import FlaskForm 
from wtforms import StringField,PasswordField,SubmitField ,BooleanField
from wtforms.validators import DataRequired, Length


class create_habit_form(FlaskForm):
    name = StringField("habit_name",validators=[DataRequired(),Length(3,200)])
    virtue = BooleanField("virtue",validators=[DataRequired()])
    submit = SubmitField("enter",validators=[DataRequired()])

class create_wish_form(FlaskForm):
    title = StringField("title",validators=[DataRequired(),Length(3,200)])
    description = StringField("description",validators=[DataRequired(),Length(3,500)])
    action_plain = StringField("action_plain",validators=[DataRequired(),Length(3,3000)])
    submit = SubmitField("enter")
