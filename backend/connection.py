import psycopg2

conn = psycopg2.connect(host="localhost", database="e-commerce", user="postgres", password="", port=5432)
cur = conn.cursor()