def perform_operation(num1, num2, operation):
    
    num1 = float(num1)
    num2 = float(num2)
    operation = str(operation).lower()
    
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "You can not divide by zero!"

        
    
    
    