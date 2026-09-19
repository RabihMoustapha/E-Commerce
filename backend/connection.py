import psycopg2
import os

def connect_db():
    return psycopg2.connect(
        dbname: "e-commerce",
        user: "postgres",
        password: "",
        host: "localhost",
        port: "5432"
    )