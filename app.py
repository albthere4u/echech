
import csv
from io import StringIO
from flask import Flask, render_template, request
from forms import CSVUploadForm
from utils import process_csv_file

# 데이터베이스를 사용한다면 models에서 db를 import합니다.
# from models import db, EnvironmentData

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # 실제 사용 시 적절한 시크릿 키로 교체해주세요.

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = CSVUploadForm()
    if form.validate_on_submit():
        csv_data = form.csvfile.data.read().decode('utf-8')
        csv_file = StringIO(csv_data)
        environment_data_list = process_csv_file(csv_file)

        return render_template('upload.html', form=form, data_list=environment_data_list)
    return render_template('upload.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
