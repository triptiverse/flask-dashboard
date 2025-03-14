from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):
    def __init__(self, user_data):
        self.id = str(user_data['_id'])
        self.username = user_data['username']
        self.role = user_data['role']
        self.initials = ''.join(word[0] for word in user_data['username'].split())
        self.userId = user_data['userId']
        if self.role == 'implement':
            self.vehicles = user_data.get('vehicles', [])
            self.implementId = user_data.get('implementId', '')
            

