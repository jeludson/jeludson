from flask import Flask, render_template, request
import sqlite3, os

app = Flask(__name__)

# ---------------------- DATABASE SETUP ----------------------
if not os.path.exists("messages.db"):
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE messages(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        message TEXT
    )
    """)
    conn.commit()
    conn.close()


# ---------------------- ROUTES ----------------------
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


@app.route("/contact", methods=["POST"])
def contact_submit():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (name, email, message) VALUES (?, ?, ?)",
                   (name, email, message))
    conn.commit()
    conn.close()

    return "Message sent successfully!"


@app.route("/messages")
def view_messages():
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM messages")
    data = cursor.fetchall()
    conn.close()

    return render_template("messages.html", messages=data)


# ---------------------- RUN ----------------------
if __name__ == "__main__":
    app.run(debug=True)
