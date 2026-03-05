from flask import Blueprint
from models import Task

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/tasks', methods=['GET'])
def get_tasks():
    return Task.query.all()
