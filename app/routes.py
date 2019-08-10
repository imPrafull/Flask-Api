from app import app, db
from firebase_admin import auth
from app.models import Teacher_location, User
from flask import request, jsonify
from functools import wraps
from datetime import date

def roles_required(user_role):
    def decorated(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            token = request.headers['Authorization']

            if not token:
                return jsonify({'message': 'Token is missing'})

            try:
                decoded_token = auth.verify_id_token(token)
                current_user = User.query.filter_by(
                    email=decoded_token['email']).first()
            except:
                return jsonify({'message': 'Token is invalid'})

            if not current_user.role == user_role:
                return jsonify({'message': 'Unauthorized access'})

            return f(*args, **kwargs)

        return wrapped

    return decorated


@app.route("/api/roles", methods=["GET"])
def get_roles():
    token = request.headers['Authorization']
    if not token:
        return jsonify({'message': 'Token is missing'})

    try:
        decoded_token = auth.verify_id_token(token)
        current_user = User.query.filter_by(
            email=decoded_token['email']).first()
    except:
        return jsonify({'message': 'Token is invalid'})

    current_user_role = current_user.role
    return jsonify({'role': current_user_role})


@app.route("/api/locations", methods=["POST"])
def add_location():
    teacher_name = request.json['teacher_name']
    class_name = request.json['class_name']
    lectures = request.json['lectures']
    arrival_time = request.json['arrival_time']
    end_time = request.json['end_time']
    date = request.json['date']

    new_location = Teacher_location(
        teacher_name, class_name, lectures, arrival_time, end_time, date)

    db.session.add(new_location)
    db.session.commit()

    return jsonify({
        'response': 'Location of ' + teacher_name+' added successfully.'
    })


@app.route("/api/locations", methods=["GET"])
def get_locations():
    today = date.today()
    formattedToday = date.isoformat(today)
    locations = Teacher_location.query.filter_by(date = formattedToday).all()
    location_list = []
    for location in locations:
        l = {
            'teacher_name': location.teacher_name,
            'class_name': location.class_name,
            'lectures': location.lectures,
            'arrival_time': location.arrival_time,
            'end_time': location.end_time
        }
        location_list.append(l)

    return jsonify(location_list)
