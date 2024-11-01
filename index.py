"""Main module - contains routing for the Flask app.
Also placed here the calculation logic as it is a simple demo app.
"""

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Simple hello world route."""
    return "Hello, World!"


@app.route("/calculate")
def calculate():
    """Calculates the result of the operation on two arguments.
    Possible operations: sum, diff, mul, div.

    Argument:
    operation -- operation to perform
    arg1 -- first argument
    arg2 -- second argument

    Returns:
    result of the operation on the two arguments
    """
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
