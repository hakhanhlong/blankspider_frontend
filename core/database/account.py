from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class ACCOUNTS(db.Document):
    username = db.StringField(max_length=255, required=True)
    email = db.StringField(max_length=255, required=True)
    fullname = db.StringField(max_length=255)
    password_hash = db.StringField(max_length=255, required=True)
    createddate = db.DateTimeField(default=datetime.now, required=True)
    lastlogin = db.DateTimeField(default=datetime.now)
    is_active = db.BooleanField(default=False)

    def __unicode__(self):
        return self.fullname

    @property
    def password(self):
        raise AttributeError('Password is not a readable attributes')

    @password.setter
    def password(self, value):
        self.password_hash = generate_password_hash(value)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_authenticated(self):
        return True

    def is_anynomous(self):
        return False

    def get_id(self):
        return unicode(self.username)

    def __repr__(self):
        return '<User %r>' % (self.username)

