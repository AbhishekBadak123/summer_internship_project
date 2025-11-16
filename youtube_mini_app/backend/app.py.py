from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)  # allows browser (frontend) to call this backend

DB_HOST = os.getenv("DB_HOST", "youtube_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "passs123")
DB_NAME = os.getenv("DB_NAME", "youtube")

def get_conn():
    return psycopg2.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)

@app.route("/videos")
def videos():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, title, filename FROM videos ORDER BY id;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{"id": r[0], "title": r[1], "filename": r[2]} for r in rows])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)