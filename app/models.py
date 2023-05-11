# from datetime import datetime
# from time import time
# from flask_login import UserMixin
# from werkzeug.security import generate_password_hash, check_password_hash
# import jwt
# from app import db, login


# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     username = db.Column(db.String(120), nullable=False)
#     newsletter = db.Column(db.Boolean, nullable=False, default=False)
#     visits = db.Column(db.Integer, nullable=False, default=0)
#
#     def __repr__(self):
#         return f'<User {self.username}>'
#
#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)
#
#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)
#
#
#     def get_reset_password_token(self, expires_in=600):
#         return jwt.encode(
#             {'reset_password': self.id, 'exp': time() + expires_in},
#             app.config['SECRET_KEY'], algorithm='HS256')
#
#     @staticmethod
#     def verify_reset_password_token(token):
#         try:
#             id = jwt.decode(token, app.config['SECRET_KEY'],
#                             algorithms=['HS256'])['reset_password']
#         except:
#             return
#         return User.query.get(id)
#
#
# @login.user_loader
# def load_user(id):
#     return User.query.get(int(id))
