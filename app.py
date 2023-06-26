from flask import Flask, render_template

app = Flask(__name__)
habits = ["Test Habit 1", "Test Habit 2"]

@app.route("/")
def index():
    return render_template("index.html", habits=habits, title="Habit Tracker - Home")

@app.route("/add", methods=["GET", "POST"])
def add_habit():
    if request.form == "POST":
        habit = request.form.get("habit")
        habits.append(habit)
    
    return render_template("add_habit.html", title="Habit Tracker - Add Habit")