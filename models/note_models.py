from lemondiary.initdb import db, create_app
from lemondiary.models.user_models import User

class Note(db.Model):
    __tablename__ = 'note'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column('userid', db.Integer, nullable=False)
    title = db.Column('title', db.Text, nullable=False)
    contents = db.Column('contents', db.Text, nullable=False)
    tag = db.Column('tag', db.String(12), nullable=True)
    create_time = db.Column('create_time', db.TIMESTAMP, nullable=False)

    def __init__(self,userid,title,contents,tag=None):
        self.userid = userid
        self.title = title
        self.contents = contents
        self.tag = tag

    def __repr__(self):
        return "<Note id=%s, author_id=%s>" % (self.id, self.user_id)

    def query_by_userid(self,userid):
        notes = Note.query.filter_by(userid=userid)
        return notes
