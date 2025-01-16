# import keyboard
# import threading

def number_entry():
    form = input("Do you need to use intergers or decimals (i:d)")
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
        result = number1 + number2
    elif symbol == "-":
        result = number1 - number2
    elif symbol == "*":
        result = number1 * number2
    elif symbol == "/" and number2 != 0 :
        result = number1 / number2
    elif number2 == 0 :
        print("Division with 0 impossible !")
    return result

# def history(number1,number2,symbol,result):
#     with open("historycalculator.txt", "r",encoding="utf8") as f :
#         text = f.read()
#     with open("historycalculator.txt", "w", encoding="utf8") as f:
#             new_entry = f"{number1} {symbol} {number2} = {result}\n"
#             f.write(new_entry + text)
    
# def display_history():
#     with open("historycalculator.txt", "r",encoding="utf8") as f :
#         text = f.read()
#     print(text)

# def reset_history():
#     with open("historycalculator.txt","w",encoding="utf8") as f :
#         f.write("")

# def keypress():
#     # while True:
#     key=keyboard.read_event()
#     if key.event_type == "down":
#         if key.name == "a":
#             display_history()
#         elif key.name == "r":
#             reset_history()

def main():
    while True:
        number1,number2=number_entry()
        symbol=symbol_entry()
        result=calcul(number1,number2,symbol)
        print(result)
        # history(number1, number2, symbol, result)
        # display_history()
# threading.Thread(target=keypress, daemon=True)

main()