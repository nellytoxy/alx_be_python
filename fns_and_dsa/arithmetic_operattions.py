def perform_operation(num1, num2, operation):
    if operation == "+":
        return num1+num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        return "invalid operation"