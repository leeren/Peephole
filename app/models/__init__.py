from app import db
from flask_security import UserMixin, RoleMixin

role_users = db.Table('role_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('roles.id')))

class Role(db.Model, RoleMixin):
    
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    roles = db.relationship('Role', secondary=role_users, backref=db.backref('users', lazy='dynamic'))
    comments = db.relationship('Comment', backref='commenter', lazy='dynamic', foreign_keys='Comment.commenter_id')
    received_comments = db.relationship('Comment', backref='received', lazy='dynamic', foreign_keys='Comment.receiver_id')
    rated_stats = db.relationship('Stat', backref='rater', lazy='dynamic', foreign_keys='Stat.rater_id')
    user_stats = db.relationship('Stat', backref='user', lazy='dynamic', foreign_keys='Stat.user_id')
    votes = db.relationship('Vote', backref='user', lazy='dynamic')
    roles = db.relationship('Role', secondary=role_users, backref='user', lazy='dynamic')
    connections = db.relationship('Connection', backref='user', lazy='joined')

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

class Connection(db.Model):

    __tablename__ = "connections"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    provider_id = db.Column(db.String(255))
    provider_user_id = db.Column(db.String(255))
    access_token = db.Column(db.String(255))
    secret = db.Column(db.String(255))
    display_name = db.Column(db.String(255))
    full_name = db.Column(db.String(255))
    profile_url = db.Column(db.String(512))
    image_url = db.Column(db.String(512))
    rank = db.Column(db.Integer)
