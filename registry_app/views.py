
from flask import render_template, redirect, request
from flask_socketio import SocketIO
from flask_wtf.csrf import CSRFProtect

from registry_app import app
from registry_app.Items import Items
from registry_app.AccessForm import AccessForm
from registry_app.SECRET_app_config import Keys, AccessCode, Names

items = Items()
access_code = AccessCode()
keys = Keys()
names = Names()

app.config["SECRET_KEY"] = keys.get_app_key()
app.config["RECAPTCHA_PUBLIC_KEY"] = keys.get_public_key()
app.config["RECAPTCHA_PRIVATE_KEY"] = keys.get_private_key()

csrf = CSRFProtect(app)

socket = SocketIO(app)

@app.route('/', methods=["GET", "POST"])
def gain_access():

    form = AccessForm()
    data = items.get_items()

    if request.method == "GET":
        form.access_code.data = ""
        form.access_code.errors = []

    if request.method == "POST":
        if form.validate_on_submit() and form.access_code.data == access_code.get_access_code():
            return render_template("registry.html", data=data, names=names)
        else:
            form.access_code.errors.append("Invalid access code or reCAPTCHA checkbox not checked!")

    return render_template("access.html", data=data, form=form, names=names)

@socket.on("mark_item_as_purchased")
def mark_item_as_purchased(data):
    items.update_item_as_purchased(data["item"])
    socket.emit("change_button_to_purchased", data={"button_id" : data["button_id"]}, broadcast=True)

@socket.on("mark_item_as_not_purchased")
def mark_item_as_purchased(data):
    items.update_item_as_not_purchased(data["item"])
    socket.emit("change_button_to_not_purchased", data={"button_id" : data["button_id"]}, broadcast=True)


"""
Pick a stroller
    Answer: Thuler Urban Glide 2

Figure out card height

Sorting button

Entry form with code and robot check

Add item streamline

Test

Publish
"""
