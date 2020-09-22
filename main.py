from CostCalculator.Calculator import CostCalculator
import flask
from flask import render_template, request
from base64 import b64encode
import hashlib
import datetime

app = flask.Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "GET":
        return render_template("index.html", post=False, paint=0, floor=0, total=0)
    else:
        try:
            width = float(request.form["width"])
            height = float(request.form["height"])
            floor = float(request.form["floor"])
            isCarpet = True if request.form["ft"] == "carpet" else False

            calc = CostCalculator()
            calc.set_wall_area(height, width)
            calc.set_floor_area(floor)
            cost = calc.calculate_costs(isCarpet)

            # return f"£{cost[0] + cost[1]}"
            return render_template("index.html", post=True, paint=round(cost[1], 2), floor=round(cost[0], 2),
                                   total=round(cost[0] + cost[1], 2))
        except:
            return render_template("index.html", post=False, paint=0, floor=0, total=0)


@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/docs", methods=["GET"])
def docs():
    return render_template("docs.html")

if __name__ == "__main__":
    context = ("ssl_crt.crt", "ssl_key.key")
    f = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    print(type(f))
    f = bytes(f.encode("utf-8"))
    x = str(hashlib.sha256(f).digest().hex())
    app.secret_key = x
    app.run("172.19.213.63", 443, ssl_context=context)