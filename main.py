import psycopg2
import os

try:
    conn = psycopg2.connect(f"host={os.getenv('POSTGRES_HOST')} dbname={os.getenv('POSTGRES_DB')} user={os.getenv('POSTGRES_USER')} password={os.getenv('POSTGRES_PASSWORD')}")
except psycopg2.Error as e:
    print("Error: could not connect to postgres database ->", e)

print("DB connected")

try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error: could not connect to postgres database ->", e)

conn.set_session(autocommit=True)

# try:
#     cur.execute("create database myfirstdb")
# except psycopg2.Error as e:
#     print("Error creating database:", e)

# create table
try:
    cur.execute("CREATE TABLE IF NOT EXISTS students (student_id int, name varchar, age int, gender varchar, subject varchar, marks int);")
except psycopg2.Error as e:
    print("Error creating table:", e)

# insert record
try:
    cur.execute("INSERT INTO students (student_id, name, age, gender, subject, marks) VALUES(%s, %s, %s, %s, %s, %s)", (1, "Blessed", 21, "Male", "Python", 99))
except psycopg2.Error as e:
    print("Error inserting record 1:", e)

try:
    cur.execute("INSERT INTO students (student_id, name, age, gender, subject, marks) VALUES(%s, %s, %s, %s, %s, %s)", (2, "Daniella", 19, "Female", "Python", 99))
except psycopg2.Error as e:
    print("Error inserting record 2:", e)

print("Record inserted")