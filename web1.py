from flask import Flask, request, render_template, jsonify, redirect

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("home.html", tips="Welcome!")


@app.route("/login", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        id = request.args.get("id", 0)
        return render_template("login.html")
    if request.method == "POST":
        data = {"username": request.form["username"],
                "password": request.form["password"]}
        # return jsonify(data)							# 将字典渲染成JSON格式再返回
        return redirect("/")							# 重定向到一个URL


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
