## Calculator program ||  IS 601 Module 2
## I did pretty much just follow along from what is in the videos from module 2
## Was I supposed to code this from scratch or just import from the repository? Played it safe here
from app.operations import addition, subtraction, multiplication, division
def calculator():

    print("IS601 Calculator")
    

    while True:

        user_input = input("Enter an operation (add, subtract, multiply, or divide) and two numbers, or 'exit' to quit: ")

        if user_input.lower() == "exit":
            print("Exiting calculator...")
            break  

        try:
            operation, num1, num2 = user_input.split()
            num1, num2 = float(num1), float(num2)
        except ValueError:
            print("Invalid input. Please follow the format: <operation> <num1> <num2>")
            continue  

        if operation == "add":
            result = addition(num1, num2)  
        elif operation == "subtract":
            result = subtraction(num1, num2) 
        elif operation == "multiply":
            result = multiplication(num1, num2)  
        elif operation == "divide":
            try:
                result = division(num1, num2) 
            except ValueError as e:
                print(e) 
                continue 
            except ZeroDivisionError:
                print("Cannot divide by zero")
                continue
        else:
            print(f"Unknown operation '{operation}'. Supported operations: add, subtract, multiply, divide.")
            continue  

        print(f"Result: {result}")