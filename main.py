from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.errorhandler(404)
def error_404(error_404):
        return render_template("404.html")

@app.route("/")
def new():
    return render_template("new.html")

#if user enter "/new",auto redirect to home page
@app.route("/new/")
def redirect_to_new():
    return redirect(url_for("new"))

if __name__ == "__main__":
    app.run(debug=True)

