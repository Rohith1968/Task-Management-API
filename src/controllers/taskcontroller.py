from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.task import Task
from utils.database import db

@jwt_required()
def create_task():
    try:
        current_user = get_jwt_identity()
        data = request.json
        new_task = Task(**data, user_id=current_user)
        db.session.add(new_task)
        db.session.commit()
        return jsonify({"message": "Task created successfully", "task": new_task.to_dict()}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@jwt_required()
def get_tasks(task_id=None):
    try:
        current_user = get_jwt_identity()
        if task_id:
            task = Task.query.filter_by(id=task_id, user_id=current_user).first()
            if not task:
                return jsonify({"error": "Task not found"}), 404
            return jsonify(task.to_dict())
        tasks = Task.query.filter_by(user_id=current_user).all()
        return jsonify([task.to_dict() for task in tasks])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@jwt_required()
def update_task(task_id):
    try:
        data = request.json
        current_user = get_jwt_identity()
        task = Task.query.filter_by(id=task_id, user_id=current_user).first()
        if not task:
            return jsonify({"error": "Task not found"}), 404
        for key, value in data.items():
            setattr(task, key, value)
        db.session.commit()
        return jsonify({"message": "Task updated successfully", "task": task.to_dict()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@jwt_required()
def delete_task(task_id):
    try:
        current_user = get_jwt_identity()
        task = Task.query.filter_by(id=task_id, user_id=current_user).first()
        if not task:
            return jsonify({"error": "Task not found"}), 404
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Task deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
