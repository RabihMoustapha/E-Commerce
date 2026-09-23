import psycopg2

conn = None
cur = None

try:
    conn = psycopg2.connect(host="localhost", database="e-commerce", user="postgres", password="R@bih12345678", port=5432)
    cur = conn.cursor()
    print("Connected")

except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()