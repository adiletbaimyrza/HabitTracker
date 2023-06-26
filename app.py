from flask import Flask, render_template, request, redirect, url_for
import datetime
from collections import defaultdict

app = Flask(__name__)
habits = ["Test Habit 1", "Test Habit 2"]
completions = defaultdict(list)


@app.context_processor
def add_calc_date_range():
    def date_range(start: datetime.datetime):
        dates = [start + datetime.timedelta(days=diff) for diff in range(-3, 4)]
        return dates
    
    return {"date_range": date_range}

@app.route("/")
def index():
    date_str = request.args.get("date")
    
    if date_str:
        selected_date = datetime.date.fromisoformat(date_str)
    else:
        selected_date = datetime.date.today()
        
    return render_template("index.html",
                           habits=habits,
                           title="Habit Tracker - Home",
                           selected_date=selected_date,
                           completions=completions[selected_date])

@app.route("/add", methods=["GET", "POST"])
def add_habit():
    if request.method == "POST":
        habit = request.form.get("habit")
        habits.append(habit)
    
    return render_template("add_habit.html",
                           title="Habit Tracker - Add Habit",
                           selected_date=datetime.date.today())
    
@app.route("/complete", methods=["POST"])
def complete():
    date_string = request.form.get("date")
    habit = request.form.get("habit_name")
    
    date = datetime.date.fromisoformat(date_string)
    completions[date].append(habit)
    
    return redirect(url_for('index', date=date_string))