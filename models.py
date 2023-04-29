from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EnvironmentData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    wind_direction = db.Column(db.Float, nullable=False)
    wind_speed = db.Column(db.Float, nullable=False)
    rainfall = db.Column(db.Float, nullable=False)
    pressure = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    soil_temperature = db.Column(db.Float, nullable=False)
    soil_moisture = db.Column(db.Float, nullable=False)
    solar_radiation = db.Column(db.Float, nullable=False)
