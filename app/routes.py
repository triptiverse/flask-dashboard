from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from flask_login import login_required, current_user
from datetime import datetime
from flask_pymongo import PyMongo
from app import mongo, dashboard_db  # This imports the mongo instance from your app package
from time import time
from functools import wraps
from werkzeug.security import generate_password_hash
from pymongo import MongoClient
from app.utils import counts  # Import counts if needed
from bson.objectid import ObjectId

bp = Blueprint('main', __name__)

# Mock dataset for implement-specific data
dummy_data = {
    "101": {"running": 5, "stop": 2, "idle": 3, "total_machines": 10, "cultivated_area": 15000, "total_area" : 18000},
    "102": {"running": 3, "stop": 4, "idle": 1, "total_machines": 8, "cultivated_area": 13000, "total_area" : 15000},
    "103": {"running": 6, "stop": 1, "idle": 2, "total_machines": 9, "cultivated_area": 14000, "total_area" : 20000}
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
@bp.route('/index')
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
    return render_template("vehicle_tracking.html")

@bp.route('/get-vehicle-locations')
@with_cache
def get_vehicle_locations():
    collections = mongo.db.list_collection_names()
    vehicle_locations = []

    for collection_name in collections:
        latest_doc = mongo.db[collection_name].find_one(
            sort=[("_id", -1)]
        )
        
        if latest_doc and "Latitude" in latest_doc and "Longitude" in latest_doc:
            status = latest_doc.get("Status", "Unknown")
            status_color = {
                "RUNNING": "success",   
                "STOP": "danger",
                "INACTIVE": "warning"
            }.get(status, "secondary")

            vehicle_locations.append({
                "vehicle_name": collection_name,
                "latitude": latest_doc["Latitude"],
                "longitude": latest_doc["Longitude"],
                "status": status,
                "status_color": status_color,
                "ign_status": latest_doc.get("IGN", "Unknown"),
                "power_status": latest_doc.get("Power", "Unknown"),
                "last_updated": latest_doc.get("GPSActualTime", "N/A"),
                "location": latest_doc.get("Location", "N/A")
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

    return render_template('vehicle_status.html', vehicles=vehicles)

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


@bp.route('/manage_users')
@login_required
def manage_users():
    # Get all users from Dashboard database
    users = list(dashboard_db.db.users.find())
    return render_template('manage_users.html', users=users, current_user=current_user)

@bp.route('/add_user', methods=['POST'])
@login_required
def add_user():
    try:
        data = request.get_json()
        
        # Check if user already exists
        existing_user = dashboard_db.db.users.find_one({'userId': data.get('userId')})
        if existing_user:
            return jsonify({
                'success': False,
                'error': 'User ID already exists'
            }), 400
        
        # Prepare user data
        user_data = {
            'userId': data.get('userId'),
            'username': data.get('username'),
            'password': generate_password_hash(data.get('password')),
            'role': data.get('role')
        }
        
        # Add implement-specific fields if role is implement
        if data.get('role') == 'implement':
            if not data.get('implementId'):
                return jsonify({
                    'success': False,
                    'error': 'Implement ID is required for implement role'
                }), 400
            
            user_data['implementId'] = data.get('implementId')
            user_data['vehicles'] = data.get('vehicles', [])
        
        # Insert user into Dashboard database
        dashboard_db.db.users.insert_one(user_data)
        
        return jsonify({'success': True}), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@bp.route('/edit_user', methods=['POST'])
@login_required
def edit_user():
    try:
        data = request.get_json()
        
        # Get original user ID and new data
        original_user_id = data.get('originalUserId')
        new_user_id = data.get('userId')
        
        # Find the user to update in Dashboard database
        user = dashboard_db.db.users.find_one({'userId': original_user_id})
        if not user:
            return jsonify({
                'success': False,
                'error': 'User not found'
            }), 404
        
        # Check if new user ID already exists (if changing user ID)
        if original_user_id != new_user_id:
            existing_user = dashboard_db.db.users.find_one({'userId': new_user_id})
            if existing_user:
                return jsonify({
                    'success': False,
                    'error': 'User ID already exists'
                }), 400
        
        # Prepare update data
        update_data = {
            'userId': new_user_id,
            'username': data.get('username'),
            'role': data.get('role')
        }
        
        # Update password only if provided
        if data.get('password'):
            update_data['password'] = generate_password_hash(data.get('password'))
        
        # Add implement-specific fields if role is implement
        if data.get('role') == 'implement':
            if not data.get('implementId'):
                return jsonify({
                    'success': False,
                    'error': 'Implement ID is required for implement role'
                }), 400
            
            update_data['implementId'] = data.get('implementId')
            update_data['vehicles'] = data.get('vehicles', [])
        elif 'implementId' in user:
            # If role changed from implement to something else, remove implement-specific fields
            dashboard_db.db.users.update_one(
                {'userId': original_user_id},
                {'$unset': {'implementId': '', 'vehicles': ''}}
            )
        
        # Update the user in Dashboard database
        dashboard_db.db.users.update_one(
            {'userId': original_user_id},
            {'$set': update_data}
        )
        
        return jsonify({'success': True}), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@bp.route('/delete_user', methods=['POST'])
@login_required
def delete_user():
    try:
        data = request.get_json()
        user_id = data.get('userid')
        
        # Delete user from Dashboard database
        result = dashboard_db.db.users.delete_one({'userId': user_id})
        
        if result.deleted_count > 0:
            return jsonify({'success': True}), 200
        else:
            return jsonify({
                'success': False,
                'error': 'User not found'
            }), 404
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

