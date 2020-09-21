from CostCalculator.Calculator import CostCalculator
import flask
from flask import render_template, request

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

            calc = CostCalculator()
            calc.set_wall_area(height, width)
            calc.set_floor_area(floor)
            cost = calc.calculate_costs(False)

            #return f"£{cost[0] + cost[1]}"
            return render_template("index.html", post=True, paint=round(cost[0], 2), floor=round(cost[1], 2), total=round(cost[0]+cost[1], 2))
        except:
            return render_template("index.html", post=False, paint=0, floor=0, total=0)



if __name__ == "__main__":
    app.run("172.19.213.63")
