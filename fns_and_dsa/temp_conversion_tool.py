def f_to_c (fahreinheit_to_celsius):
    f_to_c_value = (fahreinheit_to_celsius - 32)* (5/9)
    return f_to_c_value

def c_to_f (celsius_to_fahreinheit):
    c_to_f_value =  (celsius_to_fahreinheit * (9/5)) + 32
    return c_to_f_value


while True:
    print("Temperature you will like to convert")
    print ("1 for celsius")
    print ("2 for Fareinheit")
    print ("3 for exit")

    user_temp = input("Enter (1,2,3) for the temperature the user will like to convert to")

    if user_temp == 1:
        temp_value = input("enter the temp")
        temp_value = float(temp_value)
        print(temp_value," degree Fareinheit is", f'{f_to_c(temp_value): 2f}', "degres fareinheit")

    elif user_temp == 2:
        temp_value = input("enter the temp")
        temp_value = float(temp_value)
        
        print(temp_value," celsius is", f'{c_to_f(temp_value): 2f}', "degres celsius")

    elif temp_value == 3:
        print ("program as been closed")
        break
    else:
        print("invalid input")