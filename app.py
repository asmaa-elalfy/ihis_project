from flask import Flask, render_template, request, redirect, url_for
from receptionist import triage_patient
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///his.db"
db = SQLAlchemy(app)


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False)
    date_of_birth = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(30), nullable=False)
    chief_complaint = db.Column(db.String(300), nullable=False)
    recommended_department = db.Column(db.String(100))


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        complaint = request.form["chief_complaint"]
        department = triage_patient(complaint)
        
        new_patient = Patient(
            full_name=request.form["full_name"],
            date_of_birth=request.form["date_of_birth"],
            gender=request.form["gender"],
            phone=request.form["phone"],
            chief_complaint=complaint,
            recommended_department=department
        )
        db.session.add(new_patient)
        db.session.commit()
        return f"Patient registered successfully! Recommended department: {department}"

    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)