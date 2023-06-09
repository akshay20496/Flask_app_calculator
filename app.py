from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/math', methods=['POST'])
def math_ops():
    if (request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if ops == 'add' :
            r = num1+num2
            return "The sum of " + str(num1) + " and " + str(num2) + " is " + str(r)  
        if ops == 'subtract' :
            r = num1-num2
            return "The substraction of " + str(num1) + " and " + str(num2) + " is " + str(r)
        if ops == 'multiply' :
            r = num1*num2
            return "The multiplication of " + str(num1) + " and " + str(num2) + " is " + str(r)
        if ops == 'divide' :
            r = num1/num2
            return "The division of " + str(num1) + " and " + str(num2) + " is " + str(r)

if __name__=="__main__":
    app.run(host="0.0.0.0")
