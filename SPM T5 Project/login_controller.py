from flask import Flask, render_template, jsonify, redirect

app = Flask(__name__,template_folder ="./Templates" )


@app.route("/login")
def login():
    return render_template("login.html")



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5013, debug=True)