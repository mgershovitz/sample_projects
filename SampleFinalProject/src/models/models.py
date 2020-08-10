from src import db


class Student(object):
    def __init__(self, name, student_type):
        self.name = name
        self.student_type = student_type

    @classmethod
    def load(self, dbResponse):
        return Student(dbResponse.name, dbResponse.student_type)

    def dump(self):
        pass

    def __repr__(self):
        return "This is student %s" % self.name



class Request(object):
    def __init__(self, request_type):
        self.request_type = request_type
    def load(self):
        pass
#####################
### Students Table
### 1. Maya | Amazon | Python | team_member
### 2. Niva | Amazon | Python | student
#######################


