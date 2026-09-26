import connection
import bcrypt
from flask import Flask, request

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def create():
    password = request.form["password"]
    email = request.form["email"]

    connection.cur.execute("Select From users (email, password_hash) values (%s, %s);", (email, password))
    user = connection.cur.fetchone()

    connection.conn.commit()

    connection.cur.close()
    connection.conn.close()

    if user and bcrypt.checkpw(password.encode('utf-8'), user[0].encode('utf-8')):
        return "Logged in"
    else:
        return "Incorrect username or password", 401