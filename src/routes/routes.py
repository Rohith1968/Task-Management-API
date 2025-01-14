from flask import Flask
from flask_jwt_extended import JWTManager
from controllers.task_controller import create_task, get_tasks, update_task, delete_task
from utils.auth import authenticate
from utils.database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<username>:<password>@<host>/<database>'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

db.init_app(app)
jwt = JWTManager(app)

@app.route('/auth/login', methods=['POST'])
def login():
    return authenticate()

@app.route('/tasks', methods=['POST'])
def create():
    return create_task()

@app.route('/tasks', methods=['GET'])
@app.route('/tasks/<int:task_id>', methods=['GET'])
def read(task_id=None):
    return get_tasks(task_id)

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update(task_id):
    return update_task(task_id)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete(task_id):
    return delete_task(task_id)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
