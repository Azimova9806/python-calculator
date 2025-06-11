def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = add(a, b)
elif operation == "-":
    result = subtract(a, b)
elif operation == "*":
    result = multiply(a, b)
elif operation == "/":
    result = divide(a, b)
else:
    print("Invalid operation")

print("Result:", result)
