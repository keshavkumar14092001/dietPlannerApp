from config import db

class Profile(db.Model):
    __tablename__='profile'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable =False)
    dob = db.Column(db.String(200), nullable =False)
    email = db.Column(db.String(200), nullable =False)
    weight = db.Column(db.Double, nullable =False)
    height = db.Column(db.Double, nullable =False)
    bmi = db.Column(db.Double, nullable =False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))