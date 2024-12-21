def calculator():
    print("Welcome to the Simple Calculator.")
    print("Arithmatic Operation that are available.")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("Choose an operation.")
  
    while True:
    
        choice = input("Enter your choice (1 to 4): ")

        if choice == '1':
            result = num1 + num2
            print(f"Adittion: The result of {num1} + {num2} is {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"Subtraction: The result of {num1} - {num2} is {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"Multiplication: The result of {num1} * {num2} is {result}")
        elif choice == '4':
            if num2 == 0:
                print("Division is not allowed by zero '0'.")
            else:
                result = num1 / num2
                print(f"Division: The result of {num1} / {num2} is {result}")
        else:
            print("Invalid choice!")

        another_operation = input("Do you want to perform another opeartion? (yes/no) : ").lower() 
        if another_operation == 'no':  
            print("Thank you!") 
            break  

calculator()
