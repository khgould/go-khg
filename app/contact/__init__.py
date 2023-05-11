from flask import Blueprint

bp = Blueprint('contact', __name__)

from app.contact import forms, routes
