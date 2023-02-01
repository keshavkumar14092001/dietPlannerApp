from config import db

class Nutrition(db.Model):
    __tablename__='nutrition'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(200), nullable =False)
    protein = db.Column(db.String(200), nullable =False)
    fat = db.Column(db.String(200), nullable =False)
    carbohydrate = db.Column(db.String(200), nullable =False)
    fiber = db.Column(db.String(200), nullable =False)
    sugar = db.Column(db.String(200), nullable =False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))