def perform_operation(add, substract, multiply):
    operation = "add,substract,multiply"
    if operation == "add":
        return num1+num2
    elif operation == "substract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2
    else:
        return "invalid operation"