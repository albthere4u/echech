import csv
import io
from models import EnvironmentData

def process_csv_file(csv_file):
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

