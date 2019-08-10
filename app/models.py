from app import db, app

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text, unique = True)
    role = db.Column(db.Text, nullable = False)

    def __repr__(self):
        return '<User {}>'.format(self.name)

class Teacher_location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacher_name = db.Column(db.Text)
    class_name = db.Column(db.Text)
    lectures = db.Column(db.Integer)
    arrival_time = db.Column(db.Text)
    end_time = db.Column(db.Text)
    busy = db.Column(db.Text)
    date = db.Column(db.Text)

    def __init__(self, teacher_name, class_name, lectures, arrival_time, end_time, date):
        self.teacher_name = teacher_name
        self.class_name = class_name
        self.lectures = lectures
        self.arrival_time = arrival_time
        self.end_time = end_time
        self.date = date

    def __repr__(self):
        return '<Teacher {}>'.format(self.teacher_name)
