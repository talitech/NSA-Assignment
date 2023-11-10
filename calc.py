def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Division by zero is not allowed."

def modulus(x, y):
    if y != 0:
        return x % y
    else:
        return "Modulus by zero is not allowed."

while True:
    print("Options:")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Modulus")
    print("6: Exit")
    
    choice = input("Enter choice (1-6): ")
    
    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print("Result: ", add(num1, num2))
        elif choice == '2':
            print("Result: ", subtract(num1, num2))
        elif choice == '3':
            print("Result: ", multiply(num1, num2))
        elif choice == '4':
            print("Result: ", divide(num1, num2))
        elif choice == '5':
            print("Result: ", modulus(num1, num2))
    elif choice == '6':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")


                         
