from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, user_data):
        self.id = user_data.get('userId')  # Use userId as the ID for Flask-Login
        self.userId = user_data.get('userId')
        self.username = user_data.get('username')
        self.password = user_data.get('password')
        self.role = user_data.get('role', 'user')
        if user_data.get('role') == 'implement':
            self.implementId = user_data.get('implementId')
            self.vehicles = user_data.get('vehicles', [])
        
        # Store the MongoDB _id if it exists
        if '_id' in user_data:
            self.mongo_id = user_data['_id']
        
        # Generate initials from username
        self.initials = ''.join(word[0] for word in self.username.split()) if self.username else ''