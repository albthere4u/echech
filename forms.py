from flask_wtf import FlaskForm
from wtforms import FileField
from wtforms.validators import DataRequired

class CSVUploadForm(FlaskForm):
    csvfile = FileField("CSV 파일", validators=[DataRequired()])

