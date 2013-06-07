from lemonbook.extensions import db
from datetime import datetime


class Note(db.Model):
    __tablename__ = 'note'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column('user_id', db.Integer, nullable=False)
    contents = db.Column('contents', db.Text, nullable=False)
    create_time = db.Column('create_time', db.TIMESTAMP, nullable=False)
    date=db.Column('date',db.Text, nullable=False)

    def __init__(self,user_id,contents,date):
        self.user_id = user_id
        self.contents = contents
        self.date = date

    def __repr__(self):
        return "<Note id=%s, user_id=%s>" % (self.id, self.user_id)
    
    @classmethod
    def addNote(cls, user_id, contents, date):
        note = Note(user_id=user_id, contents=contents, date=date)
        db.session.add(note)
        db.session.commit()

    @classmethod
    def display_latest(cls, user_id):
        note = Note.query.filter_by(user_id=user_id).order_by(db.desc("create_time")).first()
        return note
    
    @classmethod
    def query_by_userid(cls, user_id):
        notes = Note.query.filter_by(user_id=user_id).all()
        #type of notes : list
        return notes

    @classmethod
    def query_by_date(cls, user_id, date):
        ''' select count(id) from note where user_id=XX and date=XX '''
        notes = Note.query.filter_by(user_id=user_id,date=date).all()
        return notes
