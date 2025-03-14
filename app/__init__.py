from flask import Flask, jsonify
from flask_pymongo import PyMongo
from flask_login import LoginManager
from bson.objectid import ObjectId
from config import Config
from app.utils import counts  # Import counts from utils

# Initialize PyMongo instances for both databases
mongo = PyMongo()  # For VehicleTracking database
dashboard_db = PyMongo()  # For Dashboard database
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config_class=Config):
    app = Flask(__name__,
                template_folder='templates',
                static_folder='static')
    
    # Configuration
    app.config.from_object(config_class)
    app.config["MONGO_URI"] = "mongodb://localhost:27017/VehicleTracking"
    app.config["DASHBOARD_MONGO_URI"] = "mongodb://localhost:27017/Dashboard"
    app.config["SECRET_KEY"] = "your-secret-key"  # Change this to a secure key

    # Initialize MongoDB connections
    mongo.init_app(app)
    
    # Initialize Dashboard database with custom config prefix
    dashboard_db.init_app(app, uri=app.config["DASHBOARD_MONGO_URI"])
    
    # Initialize Login Manager
    login_manager.init_app(app)
    
    # Register blueprints - IMPORTANT CHANGE: Import auth directly from routes
    print("Registering blueprints...")
    from app.auth.routes import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from app.routes import bp as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # Add a route to list all registered routes
    @app.route('/routes')
    def list_routes():
        routes = []
        for rule in app.url_map.iter_rules():
            routes.append({
                'endpoint': rule.endpoint,
                'methods': list(rule.methods),
                'rule': str(rule)
            })
        return jsonify(routes)
    
    print("App created successfully!")

    # User loader for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        # First try to find user in Dashboard database by userId field
        user_data = dashboard_db.db.users.find_one({'userId': user_id})
        
        # If not found, try VehicleTracking database (for backward compatibility)
        if not user_data:
            user_data = mongo.db.users.find_one({'userId': user_id})
        
        # If still not found and the ID looks like an ObjectId, try finding by _id in both databases
        if not user_data and len(user_id) == 24 and all(c in '0123456789abcdefABCDEF' for c in user_id):
            try:
                # Try Dashboard database first
                user_data = dashboard_db.db.users.find_one({'_id': ObjectId(user_id)})
                if not user_data:
                    # Then try VehicleTracking database
                    user_data = mongo.db.users.find_one({'_id': ObjectId(user_id)})
            except:
                pass
        
        if user_data:
            from app.models import User
            return User(user_data)
        return None

    # Context processor to inject counts into all templates
    @app.context_processor
    def inject_counts():
        return dict(counts=counts)

    return app 