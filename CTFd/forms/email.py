from wtforms import TextAreaField
from wtforms.validators import InputRequired

from forms import BaseForm
from forms.fields import SubmitField


class SendEmailForm(BaseForm):
    text = TextAreaField("Message", validators=[InputRequired()])
    submit = SubmitField("Send")
