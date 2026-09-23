import psycopg2

conn = psycopg2.connect(host="localhost", database="e-commerce", user="postgres", password="R@bih12345678", port=5432)
cur = conn.cursor()