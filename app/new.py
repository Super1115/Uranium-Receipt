from flask import Flask, render_template, redirect, url_for,abort
from .application import app

@app.route("/")
def new():
    return render_template("new.html")

#if user enter "/new",auto redirect to home page
@app.route("/new/")
def redirect_to_new():
    return redirect(url_for("new"))
