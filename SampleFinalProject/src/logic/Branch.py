class Branch(object):
    def __init__(self):
        self.team_members = []

    def load_team_members(self):
        students_collection = db.students()

        team_members = students_collection.find('student_type_field': 'team_member') # = [DbRespnseType(Maya,Amazin,Python,team_member)]
        for memberResponse in team_members:
            self.team_members.append(Student.load(memberResponse))

    def add_team_member(self, name):
        students_collection = db.get_collection(students)
        students_collection.insert(name, 'team_member')

    def get_requests(self):
        requests_collection = db.get_collection(requests)
        print ([Request.load(req) for req in requests_collection.findAll()])

    @classmethod
    def initiate_new_branch(self, csv_path):
        new_branch = Branch()
        new_branch.load_from_csv(csv_path)