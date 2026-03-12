from flask import Blueprint
from models import Task
from flask import  request
from flask import jsonify
from  flask import abort
from extensions import db
from datetime import datetime

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/tasks', methods=['GET'])
def get_tasks():
    ##tasks = Task.query.all()
    ##task_list = [task.to_dict() for task in tasks]
    return jsonify(tasks = [{"description": "Сделать уборку",
                        "id": 1,
                        "priority": 1,
                        "status": False,
                        "term": "2026-03-13T10:30:00"},
                   {
                       "description": "Купить творог",
                       "id": 2,
                       "priority": 3,
                       "status": False,
                       "term":"2026-04-13T10:30:00"
                   },
                    {
                     "description": "Полить цветы",
                    "id": 3,
                    "priority": 1,
                    "status": False,
                    "term": "2026-05-13T10:30:00"
                    }
                    ]
                   )

@bp.route('/add-task', methods=['POST'])
def create_task():
    data = request.get_json()

    try:
        ##task = Task.create_from_dict(data)
        ##db.session.add(task)
        ##db.session.commit()
        return jsonify({
            "description": "Приготовить лазанью",
            "id": 4,
            "priority": 1,
            "status": True,
            "term": "2026-04-15T10:30:00"
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@bp.route('/task/<int:id>', methods=['GET'])
def get_task(id):
    ##task = Task.query.get_or_404(id)
    return jsonify({
        "description": "Приготовить пирог",
        "id": 4,
        "priority": 1,
        "status": True,
        "term": "Tue, 15 Apr 2025 10:30:00 GMT"
    }), 200

@bp.route('/update-task/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.get_json() or {}


    try:
        ##task = Task.create_from_dict(task)
        ##db.session.add(task)
        ##db.session.commit()
        ##return jsonify(task.to_dict()), 200
        update_task = {
            "description": "Приготовить пасту",
            "id": id,
            "priority": 2,
            "status": True,
            "term": "Tue, 15 Apr 2025 10:30:00 GMT"
        }
        return jsonify(update_task), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@bp.route('/delete-task/<int:id>', methods=['DELETE'])
def delete_task(id):
    ##task = Task.query.get_or_404(id)
    ##db.session.delete(task)
    ##db.session.commit()
    return '', 204


