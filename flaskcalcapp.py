from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

from basiccalc import basic_calc

@app.route("/")
def home():
    return render_template("index2.html")
    
@app.route("/predict", methods=["POST"])
def predict():
    
    a = request.form['a']
    b = request.form['b']
    operation = request.form['operation']
    print("Operation:______",operation)
    
    result = basic_calc(a, b, operation)
    return render_template("index2.html", prediction_text=str(result))

app.run(host="0.0.0.0", port=8080, debug=True)

