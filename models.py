from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EnvironmentData:
    def __init__(
        self,
        timestamp,
        temperature,
        wind_direction,
        wind_speed,
        rainfall,
        pressure,
        humidity,
        soil_temperature,
        soil_moisture,
        solar_radiation,
        status1,  # status1 필드를 추가합니다.
        status2,  # status2 필드를 추가합니다.
        status3,  # status3 필드를 추가합니다.
        status4,  # status4 필드를 추가합니다.
        status5,  # status5 필드를 추가합니다.
        status6,  # status6 필드를 추가합니다.
        status7,  # status7 필드를 추가합니다.
        status8,  # status8 필드를 추가합니다.
        status9,  # status9 필드를 추가합니다.
            # 필요한 경우 여기에 추가 상태 필드를 선언합니다.
    ):
        self.timestamp = timestamp
        self.temperature = temperature
        self.wind_direction = wind_direction
        self.wind_speed = wind_speed
        self.rainfall = rainfall
        self.pressure = pressure
        self.humidity = humidity
        self.soil_temperature = soil_temperature
        self.soil_moisture = soil_moisture
        self.solar_radiation = solar_radiation
        self.status1 = status1  # status1 필드를 초기화합니다.
        self.status2 = status2  # status2 필드를 초기화합니다.
        self.status3 = status2  # status2 필드를 초기화합니다.
        self.status4 = status2  # status2 필드를 초기화합니다.
        self.status5 = status2  # status2 필드를 초기화합니다.
        self.status6 = status2  # status2 필드를 초기화합니다.
        self.status7 = status2  # status2 필드를 초기화합니다.
        self.status8 = status2  # status2 필드를 초기화합니다.
        self.status9 = status2  # status2 필드를 초기화합니다.
        # 필요한 경우 여기에 추가 상태 필드를 초기화합니다.
