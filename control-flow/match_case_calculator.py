num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /):")

match operation:
     case "+":
         results = num1 + num2
         print(f"The result is: {results}")
     case "-":
         results = num1 -num2
         print(f"The result is: {results}")
     case "*":
         results = num1 * num1
         print(f"The result is: {results}")
     case "/":
         if num2 == 0:
             print("You can't devide by zero, enter another number!")
         else:
             results = num1 /num2
             print(f"The result is: {results}")   
     case _:
         print("Invalid input, try again")
        
              
