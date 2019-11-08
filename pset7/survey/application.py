import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    # validates all fields have values, else rendertemp error.html
    name = request.form.get("name")
    human = request.form.get("humancheck")
    planet = request.form.get("planet")
    if not name or not human or not planet:
        return render_template("error.html")
    # writes the forms values to a new row in survey.csv using csv.writer
    with open("survey.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow((name, human, planet))
    # redirects user to /sheet
    return redirect("/sheet")


@app.route("/sheet", methods=["GET"])
def get_sheet():
    # reads past submissions from survey.csv using csv.reader
    with open("survey.csv", "r") as file:
        reader = csv.reader(file, delimiter=",")
        table = list(reader)
    return render_template("table.html", table=table)
    # displays values in an html table from a new template
