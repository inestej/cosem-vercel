import os
from flask import Flask, render_template, url_for, redirect, flash, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Length, ValidationError, EqualTo, Email
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
import psycopg2
from urllib.parse import urlparse

app = Flask(__name__, template_folder="templates")



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/public_dashboard')
def public_dashboard():
    return render_template('public_dashboard.html')


@app.route('/variete_ble')
def variete_ble():
    return render_template('variete_ble.html')


@app.route('/galerie')
def galerie():
    return render_template('galerie.html')




if __name__ == '__main__':
    app.run(debug=True, port=8009)
