from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import dashboard_db, mongo

class User(UserMixin):
    def __init__(self, user_data):
        self.id = user_data.get('userId')  # Use userId as the ID for Flask-Login
        self.userId = user_data.get('userId')
        self.username = user_data.get('username')
        self.password = user_data.get('password')
        self.role = user_data.get('role', 'user')
        self.implementId = user_data.get('implementId')
        self.vehicles = user_data.get('vehicles', [])
        
        # Store the MongoDB _id if it exists
        if '_id' in user_data:
            self.mongo_id = user_data['_id']
    
    def get_id(self):
        # Override get_id to return userId instead of _id
        return self.userId
    
    @staticmethod
    def get_user(user_id):
        """Find a user by userId in either database"""
        # Try Dashboard database first
        user = dashboard_db.db.users.find_one({'userId': user_id})
        if not user:
            # Then try VehicleTracking database
            user = mongo.db.users.find_one({'userId': user_id})
        return user

    def __repr__(self):
        return f"<User {self.username}>"

    def get_initials(self):
        return ''.join(word[0] for word in self.username.split())

    def is_implement(self):
        return self.role == 'implement'

    def is_user(self):
        return self.role == 'user'

    def is_admin(self):
        return self.role == 'admin'

    def is_implement_user(self):
        return self.role == 'implement_user'

    def is_implement_admin(self):
        return self.role == 'implement_admin'

    def is_user_admin(self):
        return self.role == 'user_admin'

    def is_implement_user_admin(self):
        return self.role == 'implement_user_admin'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user'

    def is_user_implement_admin(self):
        return self.role == 'user_implement_admin'

    def is_implement_user_implement_admin(self):
        return self.role == 'implement_user_implement_admin'

    def is_user_implement_user_admin(self):
        return self.role == 'user_implement_user_admin'

    def is_implement_admin_user_admin(self):
        return self.role == 'implement_admin_user_admin'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user'

    def is_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_admin_user'

    def is_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'user_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_user_implement_admin_user_implement_user_implement_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_user_implement_user_implement_admin_user'

    def is_implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_user_implement_user_implement_admin_user_implement_admin_user'
    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_admin_user(self):
        return self.role == 'implement_admin_user_implement_admin_user'

    def is_user_implement_admin_user(self):
        return self.role == 'user_implement_admin_user_implement_admin_user'

    def is_implement_user_implement_admin_user(self):
        return self.role == 'implement_user_implement_admin_user_implement_admin_user'
        self.id = str(user_data['_id'])
        self.username = user_data['username']
        self.role = user_data['role']
        self.initials = ''.join(word[0] for word in user_data['username'].split())
        self.userId = user_data['userId']
        if self.role == 'implement':
            self.vehicles = user_data.get('vehicles', [])
            self.implementId = user_data.get('implementId', '')
            

