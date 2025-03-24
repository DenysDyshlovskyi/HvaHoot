from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# Create a database connection and create a table for quizzes if it doesn't exist.
con = sqlite3.connect("hvahoot.db")
cur = con.cursor()

# Create table with corrected syntax for SQLite
cur.execute("""
    CREATE TABLE IF NOT EXISTS quizzes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        q TEXT NOT NULL,
        rs TEXT NOT NULL,
        fs1 TEXT NOT NULL,
        fs2 TEXT NOT NULL,
        fs3 TEXT NOT NULL
    )
""")


# You can insert test data if needed but consider moving this logic elsewhere.
# cur.execute("INSERT INTO quizzes (q, rs, fs1, fs2, fs3) VALUES('test question', 'test answer', 'wrong answer', 'wrong answer', 'wrong answer')")


con.commit()
con.close()

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
