from utils.database import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    status = db.Column(db.Enum("Pending", "Completed", name="status_enum"), default="Pending")
    due_date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "due_date": self.due_date.strftime("%Y-%m-%d"),
            "user_id": self.user_id
        }
