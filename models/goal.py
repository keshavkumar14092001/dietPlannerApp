from config import db

class Goal(db.Model):
    __tablename__='goal'
    id = db.Column(db.Integer, primary_key=True)
    morning_walk = db.Column(db.String(200), nullable =False)
    freehand_exercise = db.Column(db.String(200), nullable =False)
    yoga = db.Column(db.String(200), nullable =False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))