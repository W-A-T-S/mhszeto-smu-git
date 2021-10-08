import os.path
from flask import Flask, redirect, url_for, render_template
import pymongo
connection = pymongo.MongoClient(
    "18.136.194.180",
    username="spm_team",
    password="spmbestteam",
    authSource="admin",
    authMechanism="SCRAM-SHA-256",
)

db = connection["spm_aio_db"]

# collection = db["test"]
# collection.insert(dict({"hello": "how are you"}))

collection = db["learner"]
x = collection.find(dict({"is_trainer": True}))
print(list(x))





app = Flask(__name__)
@app.route('/')
def home():
    return "Hey there! Welcome to homepage" + x

@app.route("/<role>")
def user(role):
    return f"hello {role}"

@app.route("/createclass")
def createclass():
    return render_template('create_class.html')

#redirecting website with param /admin back to homepage
@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)




