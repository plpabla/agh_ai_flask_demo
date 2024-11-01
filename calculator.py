""""
This module contains the Calculator class.
It is a simple class to perform basic arithmetic operations.
"""


class Calculator:
    """
    Calculator class to perform basic arithmetic operations.
    """

    def __init__(self, op1: float, op2: float):
        self._op1 = op1
        self._op2 = op2

    def sum(self) -> float:
        """sum of 2 elements"""
        return self._op1 + self._op2

    def diff(self) -> float:
        """difference of 2 elements"""
        return self._op1 - self._op2

    def mul(self) -> float:
        """multiplication of 2 elements"""
        return self._op1 * self._op2

    def div(self) -> float:
        """division of 2 elements"""
        if self._op2 == 0:
            raise ValueError("Division by zero")
        return self._op1 / self._op2
