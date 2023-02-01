from flask import Flask, jsonify, request
from flask_cors import CORS
from config import db, SECRET_KEY
from os import environ, path, getcwd
from dotenv import load_dotenv
from models.user import User
from models.profile import Profile
from models.dietplanner import DietPlanner
from models.diettype import DietType
from models.goal import Goal
from models.nutrition import Nutrition

load_dotenv(path.join(getcwd(), '.env'))

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = False
    app.secret_key = SECRET_KEY
    db.init_app(app)
    print("DB Initialized Sucessfully")

    CORS(app)

    # test
    with app.app_context():
        # db.drop_all()
        
        # adding SignUp
        @app.route('/sign_up', methods = ['POST'])
        def sign_up():
            data = request.form.to_dict(flat=True)

            new_user = User(
                username = data["username"],
                email = data["email"],
                password = data["password"]
            )
            db.session.add(new_user)
            db.session.commit()

            return "User added successfully"

        #Adding profile
        @app.route('/add_profile',methods =['POST'])
        def add_profile():
            username = request.args.get('username')
            user = User.query.filter_by(username=username).first()

            profile_details = request.get_json()

            new_profile_details = Profile(
                name = profile_details["name"],
                dob = profile_details["dob"],
                email = profile_details["email"],
                weight = profile_details["weight"],
                height = profile_details["height"],
                user_id = user.id
            )
            db.session.add(new_profile_details)
            db.session.commit()
            return "personal Details Added Successfully"
        
        #adding diet planner

        @app.route('/add_dietplan', methods = ['POST'])
        def add_dietplan():
            username = request.args.get('username')
            user = User.query.filter_by(username=username).first()

            dietplan_details = request.get_json()

            for dietplan in dietplan_details["data"]:
                new_diatplan_details = DietPlanner(
                    time = dietplan["time"],
                    food = dietplan["food"],
                    drink = dietplan["drink"],
                    amount = dietplan["amount"],
                    user_id = user.id
                )

                db.session.add(new_diatplan_details)
            db.session.commit()
            return jsonify(msg="Diet Plan Added Successfully")

        # add diet type

        @app.route('/add_diet_type', methods = ['POST'])
        def add_diet_type():
            username = request.args.get('username')
            user = User.query.filter_by(username=username).first()

            diettype_details = request.get_json()

            for diettype in diettype_details["data"]:
                new_diettype_details = DietType(
                    foodtype = diettype["foodtype"],
                    foodname = diettype["foodname"],
                    calorie = diettype["calorie"],
                    user_id = user.id
                )

                db.session.add(new_diettype_details )
            db.session.commit()
            return jsonify(msg="Diet Type Added Successfully")
        
        #add goal
        @app.route('/add_goal', methods = ['POST'])
        def add_goal():
            username = request.args.get('username')
            user = User.query.filter_by(username=username).first()

            goal_details = request.get_json()

            new_goal_details = Goal(
                morning_walk = goal_details["morning_walk"],
                freehand_exercise = goal_details["freehand_exercise"],
                yoga = goal_details["yoga"],
                user_id = user.id
            )
            db.session.add(new_goal_details)
            db.session.commit()
            return "Your goal Added Successfully"

        # add nutrition target
        @app.route('/add_nutrition_target', methods = ['POST'])
        def add_nutrition_target():
            username = request.args.get('username')
            user = User.query.filter_by(username=username).first()

            nutrition_details = request.get_json()

            for nutritions in nutrition_details["data"]:
                new_nutritions_details =Nutrition (
                    date = nutritions["date"],
                    protein = nutritions["protein"],
                    fat = nutritions["fat"],
                    carbohydrate = nutritions["carbohydrate"],
                    fiber = nutritions["fat"],
                    sugar = nutritions["sugar"],
                    user_id = user.id
                )

                db.session.add(new_nutritions_details )
            db.session.commit()
            return jsonify(msg="nutrition details Added Successfully")

        db.create_all()
        db.session.commit()
        return app



if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)