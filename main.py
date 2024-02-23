from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temp = 47
    return {"station": station,
            "date": date,
            "Temperature": temp}


if __name__ == "__main__":
    app.run(debug=True)
