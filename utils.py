import csv
import io
from models import EnvironmentData

def process_csv_file(csv_file):
    csv_file = io.StringIO(csv_file.stream.read().decode("UTF8"), newline=None)
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # 헤더 스킵

    environment_data_list = []
    for row in csv_reader:
        data = EnvironmentData(
            timestamp=row[0],
            temperature=row[1],
            wind_direction=row[2],
            wind_speed=row[3],
            rainfall=row[4],
            pressure=row[5],
            humidity=row[6],
            soil_temperature=row[7],
            soil_moisture=row[8],
            solar_radiation=row[9]
        )
        environment_data_list.append(data)

    return environment_data_list

def evaluate_environment_data(data):
    # 각 row의 평가 범위를 설정하는 딕셔너리
    evaluation_ranges = {
        "temperature": {"normal": 10, "warning": 20},
        "wind_direction": {"normal": 10, "warning": 20},
        "wind_speed": {"normal": 10, "warning": 20},
        "rainfall": {"normal": 10, "warning": 20},
        "pressure": {"normal": 10, "warning": 20},
        "humidity": {"normal": 10, "warning": 20},
        "soil_temperature": {"normal": 10, "warning": 20},
        "soil_moisture": {"normal": 10, "warning": 20},
        "solar_radiation": {"normal": 10, "warning": 20},
    }

    results = []
    for row in data:
        result_row = []
        for index, value in enumerate(row[1:], start=1):
            key = data[0][index]  # 해당 컬럼의 키를 가져옵니다.
            value = float(value)
            if value < evaluation_ranges[key]["normal"]:
                result_row.append("정상 환경")
            elif value < evaluation_ranges[key]["warning"]:
                result_row.append("주의 요망")
            else:
                result_row.append("즉시 조치")
        results.append([row[0]] + result_row)
    return results