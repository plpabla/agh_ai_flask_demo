from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/calculate")
def calculate():
    operation = request.args.get("operation")
    arg1 = float(request.args.get("arg1", 0))
    arg2 = float(request.args.get("arg2", 0))

    if operation == "sum":
        result = arg1 + arg2
    elif operation == "diff":
        result = arg1 - arg2
    elif operation == "mul":
        result = arg1 * arg2
    elif operation == "div":
        if arg2 != 0:
            result = arg1 / arg2
        else:
            return "Error: Division by zero", 400
    else:
        return "Error: Invalid operation", 400

    return str(result)
