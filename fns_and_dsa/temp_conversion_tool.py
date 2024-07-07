FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    f_to_c_value = (fahrenheit - 32)* FAHRENHEIT_TO_CELSIUS_FACTOR
    return f_to_c_value


def convert_to_fahrenheit(celsius):
    c_to_f_value =  ( celsius* CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return c_to_f_value


while True:
    print("Temperature you will like to convert")
    print ("1 for celsius")
    print ("2 for Fareinheit")
    print ("3 for exit")

    user_temp = int(input("Enter (1,2,3) for the temperature the user will like to convert to: "))

    if user_temp == 1:
        temp_value = input("Enter the temp: ")
        temp_value = float(temp_value)
        print(temp_value," degree Fareinheit is", f'{convert_to_celsius(temp_value)}', "degres fareinheit")

    elif user_temp == 2:
        temp_value = input("enter the temp")
        temp_value = float(temp_value)
        
        print(temp_value," celsius is", f'{convert_to_fahrenheit(temp_value)}', "degres celsius")

    elif user_temp == 3:
        print ("program as been closed")
        break
    else:
        print("invalid input")