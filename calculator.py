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
        return "Error: Division by zero"
def main():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        # Get the user's choice
        choice = input("Enter choice (1/2/3/4): ")

        # Check if the choice is one of the options
        if choice in ['1', '2', '3', '4']:
            try:
                # Get the numbers from the user
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numerical values.")
                continue

            # Perform the chosen operation
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                if result == "Error: Division by zero":
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid choice. Please select a valid operation.")

        # Check if the user wants to perform another calculation
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

    print("Thank you for using the calculator")

if __name__ == "__main__":
    main()