from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

session = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/save/<num>")  # <> 안에 있는 건 URL 변수
def up(num):
    session.append(num)
    print(session)
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def save_local():
    data = request.get_json()
    print(data.get("value"))

    conn = pymysql.connect(host="localhost", user="root", passwd="q1w2e3", db="study")
    cur = conn.cursor()
    cur.execute("INSERT INTO numcount(num) VALUES (%s)", (data.get("value"),))
    conn.commit()
    conn.close()

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
