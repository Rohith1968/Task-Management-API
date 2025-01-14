from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()  # Make sure .env is in the root directory

# Flask app setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database setup
db = SQLAlchemy(app)

# Define Task model
class Task(db.Model):
    __tablename__ = 'tasks'  # Explicit table name
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.Enum('Pending', 'Completed'), nullable=False, default='Pending')
    due_date = db.Column(db.Date, nullable=False)

# Initialize tables
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create all tables based on the models
        print("Database and tables created successfully!")
