from flask import Flask, render_template, request
from datbase import insert_to_table
# import mysql.connector

app = Flask(__name__)


@app.route("/")
def hellow_world():
  return render_template("home.html")


# for database
@app.route("/submit", methods=["post"])
def get_data():
  data = request.form
  data = dict(data)
  name = data["fullname"]
  addresss = data["address"]
  email = data["email"]
  insert_to_table(name, addresss, email)
  return render_template("home.html")


if __name__ == "__main__":
  # context = ('local.crt', 'local.key')
  app.run(host="0.0.0.0", debug=True, port=3600)
