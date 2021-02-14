import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/get_contacts")
def get_contacts():
    contacts = list(mongo.db.contacts.find())
    return render_template("contacts.html", contacts=contacts)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("profile.html", username=username)
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_contacts", methods=["GET", "POST"])
def add_contact():
    if request.method == "POST":
        contact = {
            "contact_name": request.form.get("contact_name"),
            "contact_number": request.form.get("contact_number"),
            "contact_email": request.form.get("contact_email"),
            "created_by": session["user"]
        }
        mongo.db.contacts.insert_one(contact)
        flash("Contact Added")
        return redirect(url_for("get_contacts"))

    contacts = mongo.db.contacts.find().sort("contact_name", 1)
    return render_template("add_contacts.html", contacts=contacts)


@app.route("/edit_contacts/<contact_id>", methods=["GET", "POST"])
def edit_contact(contact_id):
    if request.method == "POST":
        submit = {
            "contact_name": request.form.get("contact_name"),
            "contact_number": request.form.get("contact_number"),
            "contact_email": request.form.get("contact_email"),
        }
        mongo.db.contacts.update({"_id": ObjectId(contact_id)}, submit)
        flash("Contact Updated")

    contacts = mongo.db.contacts.find_one({"_id": ObjectId(contact_id)})
    contacts = mongo.db.categories.find().sort("contact_name", 1)
    return render_template("edit_contacts.html", contacts=contacts)


@app.route("/delete_contacts/<contact_id>")
def delete_contact(contact_id):
    mongo.db.contacts.remove({"_id": ObjectId(contact_id)})
    flash("Contact Deleted")
    return redirect(url_for("get_contacts"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")), debug=True)