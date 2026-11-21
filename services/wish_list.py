from flask import Blueprint, render_template, redirect, url_for
from database import Wish_list
from scripts.forms import create_wish_form
from setup import db

wish_list_bp = Blueprint("wish_list", __name__)


@wish_list_bp.route("/")
def index():
    wishs = db.session.execute(db.select(Wish_list)).scalars().all()
    wishs_list = [
        {
            "id": wish.id,
            "title": wish.title,
            "description": wish.description,
            "action_plain": wish.action_plain,
        }
        for wish in wishs
    ]
    return render_template("wishlist.html", wishs=wishs_list, form=create_wish_form())


@wish_list_bp.route("/add", methods=["POST"])
def add():
    form = create_wish_form()
    if form.validate_on_submit():
        new_wish = Wish_list(
            title=form.title.data,
            description=form.description.data,
            action_plain=form.action_plain.data,
        )
        db.session.add(new_wish)
        db.session.commit()
        return redirect(url_for("wish_list.index"))

    # validation failed — show the errors instead of silently swallowing them
    wishs = db.session.execute(db.select(Wish_list)).scalars().all()
    wishs_list = [
        {
            "id": wish.id,
            "title": wish.title,
            "description": wish.description,
            "action_plain": wish.action_plain,
        }
        for wish in wishs
    ]
    return render_template("wishlist.html", wishs=wishs_list, form=form), 400
