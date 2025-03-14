from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify, session
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from app import mongo, dashboard_db
from ..models import User

# Define the auth Blueprint
auth = Blueprint('auth', __name__)

@auth.route('/create_test_user')
def create_test_user():
    # Check if user already exists in Dashboard database
    if dashboard_db.db.users.find_one({'username': 'admin'}):
        return 'Test user already exists!'
    
    # Create new user
    test_user = {
        'userId': 'admin',
        'username': 'admin',
        'password': generate_password_hash('admin123'),
        'role': 'admin'
    }
    
    # Insert into Dashboard MongoDB
    dashboard_db.db.users.insert_one(test_user)
    return 'Test user created successfully! UserID: admin, Password: admin123'

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # If user is already logged in, redirect to dashboard
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    if request.method == 'POST':
        userID = request.form.get('userID')
        password = request.form.get('password')
        print(userID, password)
        
        # Try to find user in Dashboard database first
        user = dashboard_db.db.users.find_one({'userId': userID})
        
        # If not found, try VehicleTracking database (for backward compatibility)
        if not user:
            user = mongo.db.users.find_one({'userId': userID})
            
        print(f"user = {user}")
        if user and check_password_hash(user['password'], password):
            user_obj = User(user)
            login_user(user_obj)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid user ID or password')
            return redirect(url_for('auth.login'))
    
    # GET request - show login form
    return render_template('auth/login.html')

@auth.route('/logout')
@login_required
def logout():
    # Log the user out
    logout_user()
    
    # Clear the session data
    session.clear()
    
    # Redirect to the login page or home page
    return redirect(url_for('auth.login'))

