import os

from datetime import datetime
from datetime import timezone

from flask import flash
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column


DATABASE = os.getenv("PG_DATABASE")
USERNAME = os.getenv("PG_USER")
PASSWORD = os.getenv("PG_PASSWORD")

SECRET_KEY = os.getenv("APP_SECRET")
DB_URL = os.getenv("PG_URL")
DB_PORT = os.getenv("PG_PORT", 5432)

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{USERNAME}:{PASSWORD}@{DB_URL}:{DB_PORT}/{DATABASE}"


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(app, model_class=Base)


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


class Todo(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    text: Mapped[str]
    pub_date: Mapped[datetime] = mapped_column(default=now_utc)


with app.app_context():
    db.create_all()


@app.route("/")
def show_all():
    select = db.select(Todo).order_by(Todo.pub_date.desc())
    todos = db.session.execute(select).scalars()
    return render_template("show_all.html", todos=todos)


@app.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "POST":
        if not request.form["title"]:
            flash("Title is required", "error")
        elif not request.form["text"]:
            flash("Text is required", "error")
        else:
            todo = Todo(title=request.form["title"], text=request.form["text"])
            db.session.add(todo)
            db.session.commit()
            flash("Todo item was successfully created")
            return redirect(url_for("show_all"))

    return render_template("new.html")

 
if __name__ == "__main__":
    app.run()
