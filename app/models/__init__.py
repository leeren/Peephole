from app import db
from flask_security import UserMixin

class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    facebook_id = db.Column(db.String)
    pic_url = db.Column(db.String)
    about_me = db.Column(db.String)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    comments = db.relationship('Comment', backref='commenter', lazy='dynamic', foreign_keys='Comment.commenter_id')
    received_comments = db.relationship('Comment', backref='received', lazy='dynamic', foreign_keys='Comment.receiver_id')
    rated_stats = db.relationship('Stat', backref='rater', lazy='dynamic', foreign_keys='Stat.rater_id')
    user_stats = db.relationship('Stat', backref='user', lazy='dynamic', foreign_keys='Stat.user_id')
    votes = db.relationship('Vote', backref='user', lazy='dynamic')

    def __repr__(self):
        return 'User: %r' % self.email

class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    commenter_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return 'Comment: %r' % self.content

class Stat(db.Model):

    __tablename__ = 'stats'

    id = db.Column(db.Integer, primary_key=True)
    rater_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    openness = db.Column(db.Integer)
    conscientiousness = db.Column(db.Integer)
    extraversion = db.Column(db.Integer) 
    agreeableness = db.Column(db.Integer)
    neuroticism = db.Column(db.Integer)

class Vote(db.Model):

    __tablename__ = 'vote'

    id = db.Column(db.Integer, primary_key=True)
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
