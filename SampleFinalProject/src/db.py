STUDENTS_TABEL_NAME = 'students'

def connect():
    return pymongo.connect(ip=127.0.0.0, port=9096)

def students():
    return self.db.get_collection(STUDENTS_TABEL_NAME)

class dbWrapper():
    def __init__(self):
        self.connection = connect()

    def query(self):
        try:
            self.db = self.connection.get_client()
        except:
            Log.error()
            gracefull

