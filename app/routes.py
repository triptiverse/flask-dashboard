from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from flask_login import login_required, current_user
from datetime import datetime
from flask_pymongo import PyMongo
from app import mongo  # This imports the mongo instance from your app package
from time import time
from functools import wraps

bp = Blueprint('main', __name__)

# Mock dataset for implement-specific data
dummy_data = {
    "101": {"running": 5, "stop": 2, "idle": 3, "total_machines": 10, "cultivated_area": 15000, "total_area" : 18000},
    "102": {"running": 3, "stop": 4, "idle": 1, "total_machines": 8, "cultivated_area": 13000, "total_area" : 15000},
    "103": {"running": 6, "stop": 1, "idle": 2, "total_machines": 9, "cultivated_area": 14000, "total_area" : 20000}
}
# Default mock data
N_machines = 19
N_implement = 10
N_cluster = 7
N_plot = 50

counts = {
    'machines': N_machines,
    'implements': N_implement,
    'clusters': N_cluster,
    'plots': N_plot
}

# Cache storage
last_update_time = 0
cached_locations = None
CACHE_DURATION = 60  # Cache duration in seconds

def with_cache(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global last_update_time, cached_locations
        current_time = time()
        
        # If cache is valid, return cached data
        if cached_locations and (current_time - last_update_time) < CACHE_DURATION:
            return cached_locations
        
        # Get fresh data
        result = func(*args, **kwargs)
        cached_locations = result
        last_update_time = current_time
        return result
    return wrapper

@bp.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    return redirect(url_for('main.dashboard'))

@bp.route('/dashboard')
@login_required
def dashboard():
    machine_states = {
        'running': 10,
        'stop': 4,
        'idle': 5
    }

    total_area = sum([data["total_area"] for data in dummy_data.values()])
    total_cultivated = sum([data["cultivated_area"] for data in dummy_data.values()])

    return render_template('dashboard.html', 
                           counts=counts,
                           machine_states=machine_states,
                           total_area=total_area,
                           total_cultivated=total_cultivated)

# New Route for Implement-Specific Data
@bp.route('/get_chart_data', methods=['POST'])
def get_chart_data():
    implement_id = request.json.get("implement_id")

    # Get data based on implement_id or provide default
    data = dummy_data.get(implement_id, {"running": 0, "stop": 0, "idle": 0, "total_machines": 0, "cultivated_area": 0})

    return jsonify({
        "machine_states": {
            "running": data["running"],
            "stop": data["stop"],
            "idle": data["idle"],
        },
        "total_machines": data["total_machines"],
        "cultivated_area": data["cultivated_area"],
        "total_area": data["total_area"]
    })


@bp.route('/vehicle-tracking')
@login_required
def vehicle_tracking():
    return render_template("vehicle_tracking.html", counts=counts)

@bp.route('/get-vehicle-locations')
@with_cache
def get_vehicle_locations():
    # Get all collections from vehicleDBdemo
    collections = mongo.db.list_collection_names()
    vehicle_locations = []

    for collection_name in collections:
        # Get the latest document from each collection
        latest_doc = mongo.db[collection_name].find_one(
            sort=[("_id", -1)]
        )
        
        if latest_doc and "Latitude" in latest_doc and "Longitude" in latest_doc:
            vehicle_locations.append({
                "vehicle_name": collection_name,
                "latitude": latest_doc["Latitude"],
                "longitude": latest_doc["Longitude"]
            })
    return jsonify(vehicle_locations)

@bp.route('/vehicle-status')
@login_required
def vehicle_status():
    collections = mongo.db.list_collection_names()
    vehicles = []

    for collection_name in collections:
        latest_doc = mongo.db[collection_name].find_one(
            sort=[("_id", -1)]
        )
        
        if latest_doc:
            status = "Unknown"
            status_color = "secondary"
            
            if "Status" in latest_doc:
                status = latest_doc["Status"]
                status_color = {
                    "RUNNING": "success",   
                    "STOP": "danger",
                    "INACTIVE": "warning"
                }.get(status, "secondary")

            # Get IGN and Power status with colors
            ign_status = latest_doc.get("IGN", "Unknown")
            ign_color = "success" if ign_status == "ON" else "danger"
            
            power_status = latest_doc.get("Power", "Unknown")
            power_color = "success" if power_status == "ON" else "danger"

            vehicles.append({
                "vehicle_name": collection_name,
                "status": status,
                "status_color": status_color,
                "ign_status": ign_status,
                "ign_color": ign_color,
                "power_status": power_status,
                "power_color": power_color,
                "last_updated": latest_doc.get("GPSActualTime", "N/A"),
                "location": latest_doc.get("Location", "N/A"),
                "latitude": latest_doc.get("Latitude", "N/A"),
                "longitude": latest_doc.get("Longitude", "N/A")
            })

    return render_template('vehicle_status.html', 
                         vehicles=vehicles,
                         counts=counts)

@bp.route('/api/vehicle/<vehicle_id>/location')
def vehicle_location(vehicle_id):
    try:
        # Debug print
        print(f"Fetching location for vehicle: {vehicle_id}")
        
        # Query the specific vehicle collection instead of 'vehicles'
        latest_doc = mongo.db[vehicle_id].find_one(
            sort=[("_id", -1)]  # Get the most recent document
        )
        
        if latest_doc:
            # Debug print
            print(f"Found vehicle data: {latest_doc}")
            
            status = latest_doc.get("Status", "Unknown")
            status_color = {
                "RUNNING": "success",   
                "STOP": "danger",
                "INACTIVE": "warning"
            }.get(status, "secondary")
            
            return jsonify({
                'vehicle_id': vehicle_id,
                'status': status,
                'status_color': status_color,
                'ign_status': latest_doc.get("IGN", "Unknown"),
                'power_status': latest_doc.get("Power", "Unknown"),
                'last_updated': latest_doc.get("GPSActualTime", "N/A"),
                'latitude': latest_doc.get("Latitude", 0),
                'longitude': latest_doc.get("Longitude", 0),
                'Location': latest_doc.get("Location", "N/A")
            })
        
        print(f"Vehicle not found: {vehicle_id}")
        return jsonify({'error': 'Vehicle not found'}), 404
        
    except Exception as e:
        print(f"Error in vehicle_location: {str(e)}")
        return jsonify({'error': str(e)}), 500




