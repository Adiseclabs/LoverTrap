# app.py
import os
import random
import io
from datetime import datetime
from functools import wraps
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, send_file
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

app = Flask(__name__)
app.config['SECRET_KEY'] = 'whba_dating_secret_key_2024'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///whba_dating.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class UserAction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(45), nullable=False)
    action_type = db.Column(db.String(100), nullable=False)
    details = db.Column(db.String(500), nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()

def get_client_ip():
    if request.headers.get('X-Forwarded-For'):
        return request.headers.get('X-Forwarded-For').split(',')[0]
    return request.remote_addr

def log_action(action_type, details=None):
    action = UserAction(ip_address=get_client_ip(), action_type=action_type, details=details)
    db.session.add(action)
    db.session.commit()
    return action

# ==============================================
# PROFILES WITH HARDCODED LOCAL IMAGE PATHS
# Place your own images in: static/images/
# ==============================================
PROFILES = [
    {"id": 1, "name": "Priya Sharma", "age": 26, "city": "Mumbai", "occupation": "Marketing Executive", 
     "bio": "Coffee enthusiast, weekend trekker, and obsessed with 90s Bollywood music.", 
     "image": "/static/images/girl1.jpg"},
    {"id": 2, "name": "Ananya Reddy", "age": 24, "city": "Bangalore", "occupation": "Software Developer", 
     "bio": "Tech geek by day, dancer by night. Love coding, cats, and trying out new cuisines.", 
     "image": "/static/images/girl2.jpg"},
    {"id": 3, "name": "Neha Kapoor", "age": 29, "city": "Delhi", "occupation": "Architect", 
     "bio": "Passionate about design, travel, and sustainable living.", 
     "image": "/static/images/girl3.jpg"},
    {"id": 4, "name": "Meera Nair", "age": 27, "city": "Chennai", "occupation": "Journalist", 
     "bio": "Storyteller at heart. Love reading, long drives, and meaningful conversations.", 
     "image": "/static/images/girl4.jpg"},
    {"id": 5, "name": "Kavya Singh", "age": 25, "city": "Pune", "occupation": "Fitness Coach", 
     "bio": "Fitness freak, foodie, and yoga enthusiast.", 
     "image": "/static/images/girl5.jpg"},
    {"id": 6, "name": "Riya Verma", "age": 28, "city": "Kolkata", "occupation": "Graphic Designer", 
     "bio": "Creative soul, love painting, photography, and exploring hidden cafes.", 
     "image": "/static/images/girl6.jpg"},
    {"id": 7, "name": "Sneha Joshi", "age": 26, "city": "Jaipur", "occupation": "Fashion Stylist", 
     "bio": "Color lover, traditional wear enthusiast, and always planning the next trip to Udaipur.", 
     "image": "/static/images/girl7.jpg"},
    {"id": 8, "name": "Aditi Kulkarni", "age": 30, "city": "Hyderabad", "occupation": "Data Scientist", 
     "bio": "Biryani connoisseur, classical dancer, and believer in strong chai conversations.", 
     "image": "/static/images/girl8.jpg"}
]

SCENARIOS = ["WIN_KEYS", "LINK_PROCEED", "INSTALL_APP", "POLICE_PANIC"]

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated

@app.route('/')
def index():
    return render_template('index.html', profiles=PROFILES)

@app.route('/api/get_scenario', methods=['POST'])
def get_scenario():
    profile_id = request.json.get('profile_id', 0)
    profile_name = next((p['name'] for p in PROFILES if p['id'] == profile_id), "Unknown")
    scenario = random.choice(SCENARIOS)
    log_action("GET_CONTACT_INITIATED", f"Profile: {profile_name} (ID: {profile_id}), Scenario: {scenario}")
    return jsonify({'scenario': scenario, 'profile_id': profile_id, 'profile_name': profile_name})

@app.route('/api/log_scenario_action', methods=['POST'])
def log_scenario_action():
    data = request.json
    log_action(data.get('action'), data.get('details', ''))
    return jsonify({'status': 'logged'})

@app.route('/scenario/proceed_link')
def scenario_proceed_link():
    log_action("LINK_PROCEED_CLICKED", "User clicked the proceed link")
    return render_template('proceed_step.html')

@app.route('/scenario/fake_payment')
def fake_payment():
    log_action("PAYMENT_LINK_CLICKED", "User clicked payment link in police panic scenario")
    return render_template('fake_payment.html')

@app.route('/download_demo')
def download_demo():
    log_action("DEMO_APP_DOWNLOADED", "User downloaded the demo app file")
    content = "WHBA Dating Demo App\n\nThis is a simulated app installation file stay chill. No actual software is installed - 0xplt : Aditya Bhosale 👀."
    return send_file(io.BytesIO(content.encode()), mimetype='text/plain', as_attachment=True, download_name='WHBA_App_Demo.txt')

# Admin routes (unchanged)
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST' and request.form.get('username') == 'admin' and request.form.get('password') == 'admin':
        session['admin_logged_in'] = True
        return redirect(url_for('admin_dashboard'))
    return render_template('admin_login.html', error="Invalid credentials" if request.method == 'POST' else None)

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin_login'))

@app.route('/admin/dashboard')
@admin_required
def admin_dashboard():
    actions = UserAction.query.order_by(desc(UserAction.timestamp)).all()
    ip_stats = db.session.query(UserAction.ip_address, db.func.count(UserAction.id)).group_by(UserAction.ip_address).all()
    return render_template('admin_dashboard.html', actions=actions, ip_stats=ip_stats)

@app.route('/admin/clear_logs', methods=['POST'])
@admin_required
def clear_logs():
    db.session.query(UserAction).delete()
    db.session.commit()
    log_action("LOGS_CLEARED", "Admin cleared all logs")
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
