def get_number(number_entry):
    while True:
        try:
            return float(input(number_entry))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_symbol(symbol_entry):
    while True:
        symbol = input(symbol_entry)
        if symbol in ["+", "-", "*", "/", "^", "%"]:
            return symbol
        print("Invalid symbol. Please enter one of (+, -, *, /, ^, %).")

def calculate(number1, number2, symbol):
    try:
        if symbol == "+":
            return number1 + number2
        elif symbol == "-":
            return number1 - number2
        elif symbol == "*":
            return number1 * number2
        elif symbol == "/":
            return number1 / number2
        elif symbol == "^":
            return number1 ** number2
        elif symbol == "%":
            return number1 % number2
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
        return None

def display_menu():
    print("\nMenu:")
    print("1. Open history")
    print("2. Clear")
    print("3. Close history")
    print("4. Quit the program")
    print("5. Perform a new calculation")

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            print("Open history selected.")

        elif choice == "2":
            print("Clear selected.")

        elif choice == "3":
            print("Close history selected.")

        elif choice == "4":
            print("Quit the program.")
            break

        elif choice == "5":
            while True:
                quantity = input("Do you want to input 2 or 3 numbers? (2/3): ")
                if quantity in ["2", "3"]:
                    break
                print("Invalid choice. Please enter '2' or '3'.")

            number1 = get_number("Enter your first number: ")
            symbol1 = get_symbol("Enter the type of calculation (+, -, *, /, ^, %): ")
            number2 = get_number("Enter your second number: ")

            if quantity == "3":
                symbol2 = get_symbol("Enter the second type of calculation (+, -, *, /, ^, %): ")
                number3 = get_number("Enter your third number: ")

                if symbol1 in ["*", "/", "^", "%"] and symbol2 in ["+", "-"]:
                    partial_result = calculate(number1, number2, symbol1)
                    if partial_result is not None:
                        result = calculate(partial_result, number3, symbol2)
                elif symbol2 in ["*", "/", "^", "%"] and symbol1 in ["+", "-"]:
                    partial_result = calculate(number2, number3, symbol2)
                    if partial_result is not None:
                        result = calculate(number1, partial_result, symbol1)
                else:
                    partial_result = calculate(number1, number2, symbol1)
                    if partial_result is not None:
                        result = calculate(partial_result, number3, symbol2)

            else:
                result = calculate(number1, number2, symbol1)

            if result is not None:
                print(f"The result is: {result}")

        else:
            print("Invalid choice. Please enter a valid option.")

main()
