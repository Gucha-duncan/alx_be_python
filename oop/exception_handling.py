
def division():
    #Handling exceptions
    
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        num1 / num2
        
    except ZeroDivisionError:
        print("You can not divide by zero, enter another number")
    
    except ValueError:
        print("Enter a valid input - Integers only")
    
    except Exception:
        print('Something Went wrong!')
    
    
    finally:
        print("Bye!")
        

division()