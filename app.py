from flask import Flask, request
from sqlalchemy import create_engine, text

app = Flask(__name__)

DATABASE_URL = "postgresql://neondb_owner:npg_cY82DrTyNlRQ@ep-divine-leaf-adasmt6m-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require"

engine = create_engine(DATABASE_URL)

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    with engine.connect() as conn:
        conn.execute(
            text("INSERT INTO messages (name, email, message) VALUES (:name, :email, :message)"),
            {"name": name, "email": email, "message": message}
        )

    return "Message sent!"
