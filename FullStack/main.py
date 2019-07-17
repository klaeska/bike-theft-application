from flask import Flask, jsonify, request, render_template, url_for, redirect, session, abort
from flask_cors import CORS
from firebase import firebase
import json 
import os
import uuid
import base64
from datetime import timedelta

app = Flask(__name__, static_url_path="", static_folder='static')
app.config['SECRET_KEY'] = '2119fc02e936287791a1796416d5ce90'
CORS(app)

# ================<< Home Page >>==============================================

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html', title='Home')

# ================<< Registration >>===========================================
@app.route('/register')
def register():
    return render_template('register.html', title='Registration')

# ================<< Login >>==================================================
@app.route('/login')
def login():
    return render_template('login.html', title='Login')

# ================<< Login Out >>==================================================
@app.route('/logout')
def logout():
    return redirect('/')

# =============================================================================

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=os.environ.get('PORT', 5000))

# =============================================================================