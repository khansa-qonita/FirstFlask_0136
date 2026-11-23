from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/home")
def home():
    return "Home page"

@app.route("/about")
def about():
    return "About us"

@app.route("/user/<name>")
def profile(name):
    return f"Hello, {escape(name)}!"

@app.route("/post/<int:post_id>")
def post(post_id):
    return f"Post #{post_id}"

# Parsing Parameter Method POST
@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        nama = request.form["nama"]
        return f"Hello, {escape(nama)}!"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)