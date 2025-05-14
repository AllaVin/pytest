import math

class Calculator:
    def sum(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def divide(self, a, b):
        if b == 0:
            raise ArithmeticError("Cannot multiply by zero")
        return a / b

    def multiply(self, a, b):
        return a * b

    def power(self, a, b=2):
        return a ** b

    def avg(self, nums):
        if len(nums) == 0:
            # raise ValueError("Cannot average an empty list")
            return 0
        s = sum(nums)
        return s / len(nums)


