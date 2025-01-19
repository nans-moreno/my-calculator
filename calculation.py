def get_number(form, number_entry):
    while True:
        try:
            if form == "i":
                return int(input(number_entry))
            elif form == "d":
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
            return number1 ^ number2
        elif symbol == "%":
            return number1 % number2
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
        return None

def main():

    while True:
        form = input("Do you want to use integers or decimals? (i/d): ").lower()
        if form in ["i", "d"]:
            break
        print("Invalid choice. Please enter 'i' for integers or 'd' for decimals.")

    while True:
        quantity = input("Do you want to input 2 or 3 numbers? (2/3): ")
        if quantity in ["2", "3"]:
            break
        print("Invalid choice. Please enter '2' or '3'.")

    number1 = get_number(form, "Enter your first number: ")
    symbol1 = get_symbol("Enter the type of calculation (+, -, *, /, ^, %): ")
    number2 = get_number(form, "Enter your second number: ")

    if quantity == "3":
        symbol2 = get_symbol("Enter the second type of calculation (+, -, *, /, ^, %): ")
        number3 = get_number(form, "Enter your third number: ")

        if symbol1 in ["*", "/","^", "%"] and symbol2 in ["+", "-"]:
            partial_result = calculate(number1, number2, symbol1)
            if partial_result is not None:
                result = calculate(partial_result, number3, symbol2)
        else:
            partial_result = calculate(number2, number3, symbol2)
            if partial_result is not None:
                result = calculate(number1, partial_result, symbol1)
    else:
        result = calculate(number1, number2, symbol1)

    if result is not None:
        print(f"The result is: {result}")

main()