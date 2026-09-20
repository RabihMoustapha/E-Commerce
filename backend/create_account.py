import connection

connection.cur.execute("Insert into users (id, name, email, password) values (%i, %s, %s, %s);", ("", "", ""))
connection.conn.commit()
connection.cur.close()
connection.conn.close()