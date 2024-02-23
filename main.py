from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    # Get certain cell
    temperature = df.loc[df["    DATE"] == date]['   TG'].squeeze() / 10
    return {"station": station,
            "date": date,
            "Temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True)
