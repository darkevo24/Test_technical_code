from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def Home():
    return render_template("index.html")


@app.route("/action/<id>", methods=["POST"])
def Action(id):
    if request.method == "POST":
        angka = request.form.get("angka")
        if id == 1:
            result = angka.split()
        else:
            result = angka
        return render_template("index.html", angka=result, turn=str(id))


if __name__ == "__main__":
    app.run(debug=True)
