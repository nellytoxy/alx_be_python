num1= float(input("enter first number "))
num2= float(input("enter second number "))
operation = input("+" "-" "/" "*")
match num1, num2:
    case _ if operation == "+":
        print("addition is", num1 + num2)
    case _ if operation == "-":
        print("substraction is", num1 - num2)
    case _ if operation == "*":
        print("multiplication is", num1 * num2)
    case _ if operation == "/":
        print("division is", num1 / num2)