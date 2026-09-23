import os
from flask import Flask, render_template

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Point template folder to the html directory
TEMPLATE_DIR = os.path.join(BASE_DIR, "frontend", "html")
# Point static folder to the frontend directory (contains css and js)
STATIC_DIR = os.path.join(BASE_DIR, "frontend")

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route("/")
def home():
    return render_template("welcome.html")

if __name__ == "__main__":
    app.run(debug=True)