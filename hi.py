from flask import Flask
from flask import render_template
from flask import make_response
from flask import request
from flask import session
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route("/")
def hello():
    resp = make_response(render_template("index.html",name="john"))
    return resp

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect(url_for("user"))

@app.route("/user")
def user():
    if "username" in session:
        return render_template("users.html", username=session["username"])
    return redirect(url_for("/"))
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

@app.route("/cat")
def test():
    return "cats are coorl <a href = '/'> slash </a>"

@app.route("/cat/<uname>")
def hey(uname):
    return "Hello %s" % uname

@app.errorhandler(404)
def page_not_found(error):
    resp = make_response(render_template("404.html"), 404)
    resp.headers["X-test"] = "this is a test"
    return resp

app.secret_key = "dasfadfadADAADf944899300a"
if __name__ == "__main__":
    app.debug = True
    app.run()