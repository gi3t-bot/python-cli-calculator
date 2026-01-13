# File name where all calculation history will be stored
history = "history.txt"


# This function shows the saved calculation history
def show_history():
    try:
        # Open the history file in read mode
        with open(history, 'r') as file:
            data = file.read()

            # If file is empty, no history is available
            if len(data) == 0:
                print("No history found!!!")
            else:
                # Print all saved calculations
                print(data)

    # If history file does not exist
    except FileNotFoundError:
        print("No history found!!!")


# This function clears all previous history
def clear_history():
    # Opening file in write mode automatically clears it
    with open(history, 'w') as file:
        pass

    print("All history cleared.")


# This function saves the calculation and result into history file
def saving_history(equation, result):
    with open(history, 'a') as file:
        file.write(f"{equation} = {result} \n")


# This function shows available commands and input format
def show_help():
    print("""
Commands:
  history         View calculation history
  clear history   Clear saved history
  exit            Exit program

Format:
  number operator number
  Example: 5 * 6
""")


# This function only performs calculation
# It does not print or save anything
def calculate(user_input):
    # Split input based on spaces
    parts = user_input.split()

    # Input must be in form: number operator number
    if len(parts) != 3:
        raise ValueError("Invalid Input format")

    # Convert numbers from string to float
    try:
        number1 = float(parts[0])
        number2 = float(parts[2])
    except ValueError:
        # If conversion fails, input is not a number
        raise ValueError("Invalid numbers")

    # Operator is the middle part
    op = parts[1]

    # Perform calculation based on operator
    if op == "+":
        return number1 + number2

    elif op == "-":
        return number1 - number2

    elif op == "*":
        return number1 * number2

    elif op == "/":
        # Division by zero check
        if number2 == 0:
            raise ZeroDivisionError
        return number1 / number2

    else:
        # Operator other than + - * /
        raise ValueError("Invalid Operator. Use only + - * /")


# Main function controls the program flow
def main():
    print("Welcome to my Simple Calculator....")

    # Infinite loop until user exits
    while True:
        user_input = input(
            "Enter calculation (+ - * /) or command (history, clear, help, exit): "
        )

        # Exit condition
        if user_input == "exit":
            print("Exit Successfull.")
            break

        # Show calculation history
        elif user_input == "history":
            print("\nRecent history...")
            show_history()

        # Clear calculation history
        elif user_input == "clear":
            print("Clearing history...")
            clear_history()

        # Show help menu
        elif user_input == "help":
            show_help()

        # If input is a calculation
        else:
            try:
                # Get result from calculate function
                result = calculate(user_input)

                # Print result
                print(f"Result = {result}")

                # Save calculation to history
                saving_history(user_input, result)

            # Handle division by zero error
            except ZeroDivisionError:
                print("Cannot divide by zero")

            # Handle all value related errors
            except ValueError as e:
                print(e)


# Program execution starts from here
main()
