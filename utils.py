import csv
from models import EnvironmentData

def process_csv_file(csv_file):
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # 헤더 스킵

    environment_data_list = []
    for row in csv_reader:
        # 각 데이터를 float 형태로 변환합니다.
        temperature = float(row[1])
        wind_direction = float(row[2])
        wind_speed = float(row[3])
        rainfall = float(row[4])
        pressure = float(row[5])
        humidity = float(row[6])
        soil_temperature = float(row[7])
        soil_moisture = float(row[8])
        solar_radiation = float(row[9])
        # 이와 같이 다른 데이터에 대해서도 float 형태로 변환한 후 필요한 경우 정상/비정상 범위를 지정할 수 있습니다.

        # 각 데이터의 상태를 결정하는 함수를 정의합니다.
        def check_temperature_status(value):
            if 27 <= value <= 29:
                return "정상"
            else:
                return "비정상"
        def check_wind_direction_status(value):
            if 190 <= value <= 210:
                return "정상"
            else:
                return "비정상"
        def check_wind_speed_status(value):
            if 190 <= value <= 210:
                return "정상"
            else:
                return "비정상"
        def check_rainfall_status(value):
            if  0 < value <= 1:
                return "정상"
            else:
                return "비정상"
        def check_pressure_status(value):
            if 991 <= value <= 993:
                return "정상"
            else:
                return "비정상"
        def check_humidity_status(value):
            if 90 <= value <= 100:
                return "정상"
            else:
                return "비정상"
        def check_soil_temperature_status(value):
            if 14 <= value <= 18:
                return "정상"
            else:
                return "비정상"
        def check_soil_moisture_status(value):
            if 102 <= value <= 112:
                return "정상"
            else:
                return "비정상"
        def check_solar_radiation_status(value):
            if 28 <= value <= 32:
                return "정상"
            else:
                return "비정상"
        # 이와 같이 다른 데이터에 대한 상태 결정 함수를 추가할 수 있습니다.

        data = EnvironmentData(
            timestamp=row[0],
            temperature=temperature,
            wind_direction=wind_direction,
            wind_speed=wind_speed,
            rainfall=rainfall,
            pressure=pressure,
            humidity=humidity,
            soil_temperature=soil_temperature,
            soil_moisture=soil_moisture,
            solar_radiation=solar_radiation,
            status1=check_temperature_status(temperature),
            status2=check_wind_direction_status(wind_direction),
            status3=check_wind_speed_status(wind_speed),
            status4=check_rainfall_status(rainfall),
            status5=check_pressure_status(pressure),
            status6=check_humidity_status(humidity),
            status7=check_soil_temperature_status(soil_temperature),
            status8=check_soil_moisture_status(soil_moisture),
            status9=check_solar_radiation_status(solar_radiation)
        )
        environment_data_list.append(data)

    return environment_data_list



