import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

from receptionist import triage_patient
from disease_predictor import predict_disease, assess_risk
from icu_specialist import assess_vitals
from radiologist import analyze_xray

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///his.db"
app.config["UPLOAD_FOLDER"] = os.path.join("static", "uploads")
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


@app.route("/gp-consultation", methods=["GET", "POST"])
def gp_consultation():
    prediction = None
    risk_info = None

    if request.method == "POST":
        fever = int(request.form["fever"])
        cough = int(request.form["cough"])
        fatigue = int(request.form["fatigue"])
        age = int(request.form["age"])

        prediction = predict_disease(fever, cough, fatigue, age)
        risk_info = assess_risk(prediction, age)

    return render_template("gp_consultation.html", prediction=prediction, risk_info=risk_info)


@app.route("/icu-dashboard", methods=["GET", "POST"])
def icu_dashboard():
    result = None

    if request.method == "POST":
        heart_rate = int(request.form["heart_rate"])
        systolic_bp = int(request.form["systolic_bp"])
        spo2 = int(request.form["spo2"])
        temperature = float(request.form["temperature"])
        respiratory_rate = int(request.form["respiratory_rate"])

        result = assess_vitals(heart_rate, systolic_bp, spo2, temperature, respiratory_rate)

    return render_template("icu_dashboard.html", result=result)


@app.route("/radiology", methods=["GET", "POST"])
def radiology():
    result = None
    image_url = None

    if request.method == "POST":
        file = request.files["xray_image"]
        if file:
            os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)

            result = analyze_xray(filepath)
            image_url = url_for("static", filename=f"uploads/{filename}")

    return render_template("radiology.html", result=result, image_url=image_url)


if __name__ == "__main__":
    app.run(debug=True)