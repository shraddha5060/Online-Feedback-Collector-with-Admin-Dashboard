# ================== IMPORTS ==================
from flask import Flask, render_template, request, redirect, url_for, Response, session, jsonify
import sqlite3
from datetime import datetime
import csv

# ================== APP CONFIG ==================
app = Flask(__name__)
app.secret_key = "admin-secret-key"
DB_NAME = "database.db"

# ================== DATABASE CONNECTION ==================
def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# ================== CREATE TABLE ==================
def create_table():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            rating INTEGER,
            comments TEXT,
            date_submitted TEXT
        )
    """)
    conn.commit()
    conn.close()

create_table()

# ================== HOME PAGE ==================
@app.route("/")
def home():
    return render_template("index.html")

# ================== SUBMIT FEEDBACK ==================
@app.route("/submit-feedback", methods=["POST"])
def submit_feedback():
    name = request.form["name"]
    email = request.form["email"]
    rating = int(request.form["rating"])
    comments = request.form["comments"]
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO feedback (name, email, rating, comments, date_submitted) VALUES (?, ?, ?, ?, ?)",
        (name, email, rating, comments, date)
    )
    conn.commit()
    conn.close()

    return redirect(url_for("home"))

# ================== ADMIN LOGIN ==================
@app.route("/admin-login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "admin123":
            session["admin"] = True
            return redirect(url_for("admin_dashboard"))
        else:
            return render_template("admin_login.html", error="Invalid credentials")

    return render_template("admin_login.html")


# ================== ADMIN DASHBOARD ==================
@app.route("/admin-dashboard")
def admin_dashboard():
    if not session.get("admin"):
        return redirect(url_for("admin_login"))

    conn = get_db_connection()
    feedbacks = conn.execute("SELECT * FROM feedback").fetchall()

    total = len(feedbacks)
    avg_rating = round(sum(f["rating"] for f in feedbacks) / total, 2) if total > 0 else 0

    ratings_count = {i: 0 for i in range(1, 6)}
    for f in feedbacks:
        if f["rating"] in ratings_count:
            ratings_count[f["rating"]] += 1

    conn.close()

    return render_template(
        "admin.html",
        feedbacks=feedbacks,
        total=total,
        avg_rating=avg_rating,
        ratings_count=ratings_count
    )

# ================== REST API ==================
@app.route("/api/feedback")
def api_feedback():
    conn = get_db_connection()
    feedbacks = conn.execute("SELECT * FROM feedback").fetchall()
    conn.close()

    data = [{
        "id": f["id"],
        "name": f["name"],
        "email": f["email"],
        "rating": f["rating"],
        "comments": f["comments"],
        "date": f["date_submitted"]
    } for f in feedbacks]

    return jsonify(data)

# ================== EXPORT CSV ==================
@app.route("/export-csv")
def export_csv():
    if not session.get("admin"):
        return redirect(url_for("admin_login"))

    conn = get_db_connection()
    feedbacks = conn.execute("SELECT * FROM feedback").fetchall()
    conn.close()

    def generate():
        yield "Name,Email,Rating,Comments,Date\n"
        for f in feedbacks:
            yield f"{f['name']},{f['email']},{f['rating']},{f['comments']},{f['date_submitted']}\n"

    return Response(
        generate(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=feedback_data.csv"}
    )

# ================== LOGOUT ==================
@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect(url_for("admin_login"))

# ================== RUN APP ==================
if __name__ == "__main__":
    app.run(debug=True)
