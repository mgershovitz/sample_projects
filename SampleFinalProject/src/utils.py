import json

from src import db
from src.models.models import Student


def get_students_for_welcome_screen():
    students_collection = db.students()
    students = students_collection.findAll()
    response = [
        repr(Student.load(dbRes)) for dbRes in students
    ]
    return json.dump(response)