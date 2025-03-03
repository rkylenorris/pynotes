from flask import Flask
from dotenv import load_dotenv
from .db_models import db
import os
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_ckeditor import CKEditor

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] =  os.getenv('FLASK_SECRET_KEY') 
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
ckeditor = CKEditor(app)



if __name__ == '__main__':
    app.run(debug=True)