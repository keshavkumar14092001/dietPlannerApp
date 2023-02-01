from config import db

class DietType(db.Model):
    __tablename__='diet_type'
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(200), nullable =False)
    calorie = db.Column(db.Integer, nullable =False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))