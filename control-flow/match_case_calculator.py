num1 = float(input("enter first number \n"))
num2 = float(input("enter second number \n"))
operation = input("addition, " "substraction, " "multiplication, " "division " "\n")
match operation:
    case operation if operation == "addition":
        print("result is", num1 + num2)
    case operation if operation == "substraction":
        print("result is", num1 - num2)
    case operation if operation == "multiplication":
        print("result is", num1 * num2)
    case operation if operation == "division":
        print("result is", num1 / num2)
    case _:
        print("Cannot divide by zero")