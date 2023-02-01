from config import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable = False)
    email = db.Column(db.String(200), nullable = False)
    password = db.Column(db.String(200), nullable = False)
    profile = db.relationship('Profile',backref = 'user')
    dietplanner = db.relationship('DietPlanner',backref = 'user')
    diettype = db.relationship('DietType',backref = 'user')
    goal = db.relationship('Goal',backref = 'user')
    nutrition = db.relationship('Nutrition',backref = 'user')

    def verify_password(self, passw):
        return self.password==passw
    
    