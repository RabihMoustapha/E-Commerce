import connection
import bcrypt
from flask import Flask, request

app = Flask(__name__, template_folder="../frontend/html", static_folder="../frontend")

@app.route("api/login", methods=["POST"])
def login():
    data = request.get_json()
    password = data.get("password")
    email = data.get("email")

    connection.cur.execute("Select * From users where email = %s and password_hash = %s", (email, password))
    user = connection.cur.fetchone()

    connection.cur.close()
    connection.conn.close()

    if user:
        return "Logged in"
    else:
        return "Incorrect username or password", 401