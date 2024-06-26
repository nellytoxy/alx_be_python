num1 = int(input("Enter the first number\n"))
num2 = int(input("enter second the number\n"))
operation = input("addition, " "substraction, " "multiplication, " "division " "\n")
match operation:
    case operation if operation == "addition":
        print("result is", num1 + num2)
    case operation if operation == "substract":
        print("result is", num1 - num2)
    case operation if operation == "multiply":
        print("result is", num1 * num2)
    case operation if operation == "divide":
        print("result is", num1 / num2)
    case _:
        print("Cannot divide by zero.")