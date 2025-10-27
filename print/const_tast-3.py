class Calculator:
    # Method for addition
    def add(self, a, b):
        return a + b

    # Method for subtraction
    def sub(self, a, b):
        return a - b

    # Method for multiplication
    def mul(self, a, b):
        return a * b

    # Method for division
    def div(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error! Division by zero."

# Create object of Calculator class
calc = Calculator()

# Test the methods
print("Addition:", calc.add(10, 5))
print("Subtraction:", calc.sub(10, 5))
print("Multiplication:", calc.mul(10, 5))
print("Division:", calc.div(10, 5))
print("Division by zero:", calc.div(10, 0))
