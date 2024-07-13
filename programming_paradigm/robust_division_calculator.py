def safe_divide(numerator, denominator):
    try:
       result = float(numerator)/float(denominator)
       return (result)
    except ZeroDivisionError as Exception:
        print ("Error: Cannot divide by zero.")
    except ValueError as Exception:
        print ("Error: Please enter numeric values only.")