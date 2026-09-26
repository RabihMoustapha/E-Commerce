import connection
from flask import Flask, request

app = Flask(__name__, template_folder="../frontend/html", static_folder="../frontend")

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return "Invalid request: JSON body required", 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return "Email and password are required", 400

    if connection.cur is None or connection.conn is None:
        return "Database connection error", 500

    try:
        # Plain password comparison because create_account.py currently stores
        # the password directly in password_hash.
        connection.cur.execute(
            "SELECT * FROM users WHERE email = %s AND password_hash = %s",
            (email, password)
        )
        user = connection.cur.fetchone()
    except Exception as e:
        print("Database error during login:", e)
        return "Database error", 500

    if user:
        return "Logged in"
    else:
        return "Incorrect username or password", 401