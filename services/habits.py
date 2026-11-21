from database import Habits
from flask import Blueprint, render_template, redirect, url_for
from scripts.forms import create_habit_form
from datetime import date
from setup import db

habits_bp = Blueprint("habits", __name__)


@habits_bp.route("/")
def index():
    habits = db.session.execute(
        db.select(Habits)
    ).scalars().all()

    today = date.today()

    habits = [
        {
            "id": habit.id,
            "name": habit.name,
            "virtue": habit.virtue,
            "started_sequencie": habit.started_sequencie,
            "days": (today - habit.started_sequencie.date()).days
        }
        for habit in habits
    ]

    return render_template(
        "habits.html",
        habits=habits,
        form=create_habit_form()
    )


@habits_bp.route("/add", methods=["POST"])
def add():
    form = create_habit_form()

    if form.validate_on_submit():

        habit_name = form.name.data
        habit_virtue = form.virtue.data

        habit = Habits(
            name=habit_name,
            virtue=habit_virtue,
            started_sequencie=date.today()
        )

        db.session.add(habit)
        db.session.commit()

    return redirect(url_for("habits.index"))


@habits_bp.route("/<int:habit_id>/reset", methods=["POST"])
def reset(habit_id):
    habit = db.session.get(Habits, habit_id)

    if habit is None:
        return redirect(url_for("habits.index"))

    habit.started_sequencie = date.today()

    db.session.commit()

    return redirect(url_for("habits.index"))
