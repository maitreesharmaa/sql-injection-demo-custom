from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def get_data():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM data") 
    data = c.fetchall()
    conn.close()
    return data

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    name = data.get("name")
    password = data.get("password")

    if not name or not password:
        return jsonify({"message": "Name and password are required."}), 400
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    try:
        c.execute("INSERT INTO users (name, password) VALUES (?, ?)", (name, password))
        conn.commit()
        return jsonify({"message": "Registration succesful."})
    except sqlite3.IntegrityError:
        return jsonify({"message": "User already exists."}), 409
    finally:
        conn.close()

@app.route("/search")
def search():
    code = request.args.get('code')
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    try:
        statement = "SELECT * FROM data WHERE data = '" + code + "'"
        c.execute(statement)
        found = c.fetchall()
    except sqlite3.Error as e:
        return str(e) + f"<br>{statement}"
    return jsonify(found)

@app.route("/api/login")
def api_login():
    name = request.args.get("name")
    password = request.args.get("password")

    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    try:
        query = f"SELECT * FROM users WHERE name = '{name}' AND password = '{password}'"
        print("QUERY BEING EXECUTED:", query)
        c.execute(query)
        user = c.fetchone()
    except Exception as e:
        return f"Error: {e}<br>Query: {query}"
    finally:
        conn.close()

    if user:
        return f"Welcome, {name}!"
    else:
        return "Invalid credentials"
    

@app.route("/login")
def login():
    return open("login.html").read()

@app.route("/all")
def all_data():
    return jsonify(get_data())

@app.route("/")
def main():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

