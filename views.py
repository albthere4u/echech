from flask import Flask, render_template, request
from forms import CSVUploadForm
from utils import process_csv_file
import csv
import io

# 데이터베이스를 사용한다면 models에서 db를 import합니다.
# from models import db, EnvironmentData


app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = CSVUploadForm()
    environment_data_list = None
    if form.validate_on_submit():
        csv_file = form.csvfile.data
        environment_data_list = process_csv_file(csv_file)

        # 환경 데이터 저장
        # 데이터베이스를 사용하는 경우, 아래 주석을 해제하고 실행합니다.
        # for data in environment_data_list:
        #     db.session.add(data)
        # db.session.commit()

    return render_template('upload.html', form=form, data_list=environment_data_list)