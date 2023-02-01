from config import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable = False)
    email = db.Column(db.String(200), nullable = False)
    password = db.Column(db.String(200), nullable = False)
    profile = db.relationship('Profile',backref = 'user')
    diet_planner = db.relationship('Diet_Planner',backref = 'user')
    diet_type = db.relationship('Diet_Type',backref = 'user')
    
    