import connection
import bcrypt
from flask import Flask, request

app = Flask(__name__, template_folder="../frontend/html", static_folder="../frontend")

@app.route("/api/create_account", methods=["POST"])
def create():
    id = request.form.get("id")
    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]

    connection.cur.execute("Insert into users (id, username, email, password_hash) values (%i, %s, %s, %s);", (id, username, email, password))
    user = connection.cur.fetchone()

    connection.conn.commit()

    connection.cur.close()
    connection.conn.close()

    if user:
        return "User created successfully"
    else:
        return "User does not exist"