from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('data_small/stations.txt', skiprows=17)
ndf = df[['STAID', 'STANAME                                 ']]


@app.route("/")
def index():
    return render_template("index.html", data=ndf.to_html())


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    # Get certain cell
    temperature = df.loc[df["    DATE"] == date]['   TG'].squeeze() / 10
    return {"station": station,
            "date": date,
            "Temperature": temperature}


@app.route("/api/v1/<station>")
def method2(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient="records")
    return result


@app.route("/api/v1/yearly/<station>/<year>")
def method3(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    # Changing dates from type int to string
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return result


if __name__ == "__main__":
    app.run(debug=True)
