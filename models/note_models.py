from lemonbook.initdb import db, create_app

class Note(db.Model):
    __tablename__ = 'note'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column('userid', db.Integer, nullable=False)
    contents = db.Column('contents', db.Text, nullable=False)
    create_time = db.Column('create_time', db.TIMESTAMP, nullable=False)

    def __init__(self,userid,contents):
        self.userid = userid
        self.contents = contents

    def __repr__(self):
        return "<Note id=%s, userid=%s>" % (self.id, self.userid)

    def addNote(self, userid, contents):
        note = Note(userid=userid, contents=contents)
        db.session.add(note)
        db.session.commit()

    def query_by_userid(self,userid):
        notes = Note.query.filter_by(userid=userid).all()
        #type of notes : list
        return notes
