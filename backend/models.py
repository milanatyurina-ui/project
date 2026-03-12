from extensions import db
from datetime import datetime

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    description = db.Column(db.String, nullable=True)
    priority = db.Column(db.Integer, nullable=False)
    term = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    def to_dict(self):
        return {'id':self.id,
                'description':self.description,
                'priority':self.priority,
                'term':self.term,
                'status':self.status
                }

    @classmethod
    def create_from_dict(cls, data:dict):
        if not isinstance(data, dict):
            raise ValueError('data must be a dictionary')

        required_fields = ['description','priority','term']
        for field in required_fields:
            if field not in data:
                raise ValueError(f'Missing required field {field}')

        if not str(data.get('description', '')).strip():
            raise ValueError(f'Missing description')

        try:
            priority = int(data['priority'])
        except (ValueError, TypeError):
            raise ValueError('Priority must be an integer')

        try:
            term_str = str(data['term']).replace('Z','+00:00')
            term_date = datetime.fromisoformat(term_str)
        except (ValueError, TypeError):
            raise ValueError('Invalid date format. Use ISO format (YYYY-MM-DDTHH:MM:SS)')

        status = data.get('status', False)
        if not isinstance(status, bool):
            raise ValueError('Status must be a boolean')

        task = cls(
            description=str(
                description=str(data['description']).strip(),
                priority=priority,
                term=term_date,
                status=status)
        )
        return task
