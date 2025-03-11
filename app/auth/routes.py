from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from app import mongo
from ..models import User

auth = Blueprint('auth', __name__)

@auth.route('/create_test_user')
def create_test_user():
    # Check if user already exists
    if mongo.db.users.find_one({'username': 'admin'}):
        return 'Test user already exists!'
    
    # Create new user
    test_user = {
        'username': 'admin',
        'password': generate_password_hash('admin123'),
        'role': 'admin'
    }
    
    # Insert into MongoDB
    mongo.db.users.insert_one(test_user)
    return 'Test user created successfully! Username: admin, Password: admin123'

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # If user is already logged in, redirect to dashboard
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = mongo.db.users.find_one({'username': username})
        
        if user and check_password_hash(user['password'], password):
            user_obj = User(user)
            login_user(user_obj)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
    
    # GET request - show login form
    return render_template('auth/login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

