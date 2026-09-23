import connection

def create(user_id, user_name, user_email, user_password):
    return connection.cur.execute("Insert into users (id, name, email, password) values (%i, %s, %s, %s);", (user_id, user_name, user_email, user_password))

connection.conn.commit()
connection.cur.close()
connection.conn.close()