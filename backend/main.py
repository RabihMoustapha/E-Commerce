import os
from flask import Flask, render_template

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

app = Flask(__name__, template_folder=FRONTEND_DIR, static_folder=FRONTEND_DIR)

@app.route("/")
def home():
    return render_template("welcome.html")

if __name__ == "__main__":
    app.run(debug=True)