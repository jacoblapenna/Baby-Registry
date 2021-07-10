from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, validators

class AccessForm(FlaskForm):
      access_code = StringField("Enter Access Code:", [validators.DataRequired(), validators.Length(max=255)], render_kw={"placeholder" : "access code", "autocomplete" : "off"})
      recaptcha = RecaptchaField()
