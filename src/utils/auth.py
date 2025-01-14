from flask import request, jsonify
from flask_jwt_extended import create_access_token
import hashlib

users = {"testuser": hashlib.sha256("password".encode()).hexdigest()}

def authenticate():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if username in users and users[username] == hashed_password:
        token = create_access_token(identity=username)
        return jsonify({"access_token": token}), 200
    return jsonify({"error": "Invalid credentials"}), 401
