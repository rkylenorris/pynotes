from flask import Flask
from dotenv import load_dotenv
from .db_models import db
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] =  os.getenv('FLASK_SECRET_KEY') 
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
db.init_app(app)





if __name__ == '__main__':
    app.run(debug=True)