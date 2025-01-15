def number_entry():
    form = input("Do you need to ude intergers or decimals (i:d)")
    if form == "i":
        number1 = int(input("Enter your first number:"))
        number2 = int(input("Enter the second number:"))
    elif form == "d" :
        number1 = float(input("Enter your first number :"))
        number2 = float(input("Enter your second number :"))
    return number1, number2

def symbol_entry():
    symbol = input("Enter the type of calculation you want to do (+,-,*,/):")
    if symbol != "+" and symbol !="-" and symbol !="*" and symbol !="/":
        print("Invalid symbol, try again !")
    return symbol

def calcul(number1,number2,symbol):
    if symbol == "+":
        print(number1 + number2)
    elif symbol == "-":
        print(number1 - number2)
    elif symbol == "*":
        print(number1 * number2)
    elif symbol == "/" and number2 != 0 :
        print(number1 / number2)
    elif number2 == 0 :
        print("Division with 0 impossible !")

def main():
    number1,number2=number_entry()
    symbol=symbol_entry()
    calcul(number1,number2,symbol)

main()