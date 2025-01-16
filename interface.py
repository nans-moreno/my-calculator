def number_entry():
    form = input("Do you need to use integers or decimals (i/d)? ")
    if form == "i":
        try:
            number1 = int(input("Enter your first number: "))
            number2 = int(input("Enter the second number: "))
        except ValueError:
            print("Please enter only numbers.")
            return number_entry()
    elif form == "d":
        try:
            number1 = float(input("Enter your first number: "))
            number2 = float(input("Enter the second number: "))
        except ValueError:
            print("Please enter only numbers.")
            return number_entry()
    else:
        print("Invalid input. Please enter 'i' for integers or 'd' for decimals.")
        return number_entry()
    return number1, number2

def symbol_entry():
    symbol = input("Enter the type of calculation you want to do (+, -, *, /): ")
    if symbol not in ["+", "-", "*", "/"]:
        print("Invalid symbol. Please enter one of the following: +, -, *, /")
        return symbol_entry()
    return symbol

def calcul(number1, number2, symbol):
    if symbol == "+":
        print(f"{number1} + {number2} = {number1 + number2}")
    elif symbol == "-":
        print(f"{number1} - {number2} = {number1 - number2}")
    elif symbol == "*":
        print(f"{number1} * {number2} = {number1 * number2}")
    elif symbol == "/":
        if number2 != 0:
            print(f"{number1} / {number2} = {number1 / number2}")
        else:
            print("Division by zero is not allowed!")

def main():
    number1, number2 = number_entry()
    symbol = symbol_entry()
    calcul(number1, number2, symbol)

main()
