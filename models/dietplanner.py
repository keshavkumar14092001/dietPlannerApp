from config import db

class DietPlanner(db.Model):
    __tablename__='dietplan'
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(200), nullable =False)
    food = db.Column(db.String(200), nullable =False)
    drink = db.Column(db.String(200), nullable =False)
    amount = db.Column(db.String(200), nullable =False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))