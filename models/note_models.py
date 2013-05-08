from diary.initdb import db, create_app

class Note(db.Model):
    __tablename__ == 'note'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column('userid', db.Interger, nullable=False)
    title = db.Column('title', db,Text, nullable=False)
    contents = db.Column('contents', db.Text, nullable=False)
    tag = db.Column('tag', db.String(12), nullable=True)
    create_time = db.Column('create_time', db.TIMESTAMP, nullable=False)

    def __init__(self,userid,title,contents,tag=None,create_time):
        self.userid = userid
        self.title = title
        self.contents = contents
        self.tag = tag
        self.create_time = create_time

    def __repr__(self):
        return "<Note id=%s, author_id=%s>" % (self.id, self.user_id)
