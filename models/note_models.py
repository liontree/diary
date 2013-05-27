from lemonbook.extensions import db

class Note(db.Model):
    __tablename__ = 'note'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column('user_id', db.Integer, nullable=False)
    contents = db.Column('contents', db.Text, nullable=False)
    create_time = db.Column('create_time', db.TIMESTAMP, nullable=False)

    def __init__(self,user_id,contents):
        self.user_id = user_id
        self.contents = contents

    def __repr__(self):
        return "<Note id=%s, user_id=%s>" % (self.id, self.user_id)
    
    @classmethod
    def addNote(cls, user_id, contents):
        note = Note(user_id=user_id, contents=contents)
        db.session.add(note)
        db.session.commit()

    @classmethod
    def display_latest(cls, user_id):
        note = Note.query.filter_by(user_id=user_id).order_by(db.desc("create_time")).first()
        return note

    def query_by_userid(cls, user_id):
        notes = Note.query.filter_by(user_id=user_id).all()
        #type of notes : list
        return notes
