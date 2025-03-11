from flask import Flask
from flask_pymongo import PyMongo
from flask_login import LoginManager
from .config import Config
from bson.objectid import ObjectId

# Initialize MongoDB and LoginManager
mongo = PyMongo()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__,
                template_folder='templates',
                static_folder='static')
    
    # Configuration
    app.config.from_object(Config)
    app.config["MONGO_URI"] = "mongodb://localhost:27017/VehicleTracking"
    app.config["SECRET_KEY"] = "your-secret-key"  # Change this to a secure key

    # Initialize MongoDB with app
    mongo.init_app(app)
    
    # Initialize Login Manager
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    # Register blueprints
    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)
    
    from .auth.routes import auth
    app.register_blueprint(auth)
    
    # User loader for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        from .models import User
        user_data = mongo.db.users.find_one({'_id': ObjectId(user_id)})
        return User(user_data) if user_data else None

    return app 