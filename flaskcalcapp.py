from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

from basiccalc import basic_calc

@app.route("/")
def home():
    return render_template("index2.html")
    
@app.route("/show_res", methods=["POST"])
def show_res():
    
    a = request.form['a']
    b = request.form['b']
    operation = request.form['operation']
    print("Operation:______",operation)
    
    result = basic_calc(a, b, operation)
    return render_template("index2.html", show_result=str(result))



