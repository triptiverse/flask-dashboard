import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    MONGO_URI = "mongodb://localhost:27017/VehicleTracking"
    DASHBOARD_MONGO_URI = "mongodb://localhost:27017/Dashboard" 