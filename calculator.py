import json

history = []

def get_number(number_entry):
    while True:
        try:
            return float(input(number_entry))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_symbol(operator_entry):
    while True:
        operator = input(operator_entry)
        if operator in ["+", "-", "*", "/", "^", "%"]:
            return operator
        print("Invalid symbol. Please enter one of (+, -, *, /, ^, %).")

def calculate(number1, number2, operator):
    try:
        if operator == "+":
            return number1 + number2
        elif operator == "-":
            return number1 - number2
        elif operator == "*":
            return number1 * number2
        elif operator == "/":
            return number1 / number2
        elif operator == "^":
            return number1 ** number2
        elif operator == "%":
            return number1 % number2
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
        return None

def add_to_history(number1, operator1, number2, operator2, number3, result, history):
    if operator2 is None and number3 is None:
        history.append(
            {
                "number1": number1,
                "operator": operator1,
                "number2": number2,
                "operation": f"{number1}{operator1}{number2}",
                "result": result
            }
        )
    else:
        history.append(
            {
                "number1": number1,
                "operator1": operator1,
                "number2": number2,
                "operator2": operator2,
                "number3": number3,
                "operation": f"{number1}{operator1}{number2}{operator2}{number3}",
                "result": result
            }
        )

def export_to_json(history, filename):
    with open(filename, 'w') as f:
        json.dump(history, f, indent=4)

def read_from_json(filename):
    try:
        with open(filename, 'r') as f:
            history = json.load(f)
            return history
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return None

def clear_json_file(filename):
    try:
        with open(filename, 'w') as f:
            f.write("[]")
            print("History successfully cleared.")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

def display_menu():
    print("\nMenu:")
    print("1. Perform a calculation")
    print("2. View history")
    print("3. Clear history")
    print("4. Quit the program")

def main():
    while True:
        display_menu()
        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            while True:
                quantity = input("\nDo you want to input 2 or 3 numbers? (2/3): ")
                if quantity in ["2", "3"]:
                    break
                print("\nInvalid choice. Please enter '2' or '3'.")

            number1 = get_number("\nEnter your first number: ")
            operator1 = get_symbol("\nEnter the type of calculation (+, -, *, /, ^, %): ")
            number2 = get_number("\nEnter your second number: ")

            if quantity == "3":
                operator2 = get_symbol("\nEnter the second type of calculation (+, -, *, /, ^, %): ")
                number3 = get_number("\nEnter your third number: ")

                if operator1 in ["*", "/", "^", "%"] and operator2 in ["+", "-"]:
                    partial_result = calculate(number1, number2, operator1)
                    if partial_result is not None:
                        result = calculate(partial_result, number3, operator2)
                elif operator2 in ["*", "/", "^", "%"] and operator1 in ["+", "-"]:
                    partial_result = calculate(number2, number3, operator2)
                    if partial_result is not None:
                        result = calculate(number1, partial_result, operator1)
                else:
                    partial_result = calculate(number1, number2, operator1)
                    if partial_result is not None:
                        result = calculate(partial_result, number3, operator2)

                if result is not None:
                    add_to_history(number1, operator1, number2, operator2, number3, result, history)

            else:
                result = calculate(number1, number2, operator1)
                if result is not None:
                    add_to_history(number1, operator1, number2, None, None, result, history)

            export_to_json(history, 'calcul_history.json')
            if result is not None:
                print(f"\nThe result is: {result}")

        elif choice == "2":
            print("\nView history selected.")
            saved_history = read_from_json('calcul_history.json')
            if saved_history:
                for entry in saved_history:
                    print(f"\nOperation: {entry['operation']}\nResult: {entry['result']}\n")

        elif choice == "3":
            print("\nClear history selected.")
            clear_json_file('calcul_history.json')


        elif choice == "4":
            print("\nGoodbye !")
            break

        else:
            print("\nInvalid choice. Please enter a valid option.")

main()