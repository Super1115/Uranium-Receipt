from flask import Flask, render_template,request
from .application import app

@app.errorhandler(404)
def error_404(e):
        return render_template("404.html")

@app.errorhandler(403)
def error_403(e):
        return render_template("403.html")

@app.errorhandler(400)
def error_400(e):
        return render_template("400.html")