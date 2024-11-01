"""Main module - contains routing for the Flask app.
Also placed here the calculation logic as it is a simple demo app.
"""

from flask import Flask, request
from calculator import Calculator

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

    if operation is None:
        return "Error: No operation provided", 400

    if operation not in ["sum", "diff", "mul", "div"]:
        return "Error: Invalid operation", 400

    if operation == "div" and arg2 == 0:
        return "Error: Division by zero", 400

    calculator = Calculator(arg1, arg2)
    result = None
    if operation == "sum":
        result = calculator.sum()
    elif operation == "diff":
        result = calculator.diff()
    elif operation == "mul":
        result = calculator.mul()
    elif operation == "div":
        result = calculator.div()

    return str(result)
