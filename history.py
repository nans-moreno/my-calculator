import json

history = []

"""def calcul(number_1, operator, number_2):
    if operator == "+":
        return number_1 + number_2
    if operator == "-":
        return number_1 - number_2
    if operator == "*":
        return number_1 * number_2
    if operator == "/":
        if number_2 != 0:
            return number_1 / number_2
        else:
            print("Invalid.")
    if operator == "%":
        if number_2 != 0:
            return number_1 % number_2
        else:
            print("Invalid.")
    else:
        print("Operator incorrect.")""" 
#Petite calculette pour tester vite fait.


def add_to_history(number_1, operator, number_2, result, history):
    history.append(
        {
            "number1": number_1,
            "operator": operator,
            "number2": number_2,
            "operation": f"{number_1}{operator}{number_2}",
            "result": result
        }
        )
    
"""    print(history)
ajouter_a_historique(1,'+', 5, 6, historique)
ajouter_a_historique(1,'-', 1, 0, historique)
print(calcul(historique[0].get("number1"), historique[0].get("operator"), historique[0].get("number2")))
print(historique[0].get("operation"))
print(historique[1].get("operation"))""" 
#Ce gros bloc sert uniquement à tester les trucs. Je le laisse pour que vous puissiez tester si vous voulez.



def export_to_json(history, filename):
  with open(filename, 'w') as f:
    json.dump(history, f, indent=4)

"""export_to_json(history, 'calcul_history.json')"""#A utiliser dans l'interface 


def read_from_json(filename):
  try:
    with open(filename, 'r') as f:
      history = json.load(f)
      return history
  except FileNotFoundError:
    print(f"The file {filename} does not exist.")
    return None

"""history = read_from_json('calcul_history.json')"""#A utiliser dans l'interface 

def clear_json_file(filename):
  try:
    with open(filename, 'w') as f:
        pass
  except FileNotFoundError:
    print(f"The file {filename} does not exist.")

"""clear_json_file('calcul_history.json')"""#A utiliser dans l'interface 



'''
while True:
    print("""
    Options :
1. Calcul
2. Show history
3. Delete history
4. Quit the program
          """)

    menu_choice = input("\nSelect an option : ")
    if menu_choice == "1":
        operation_choice = input("Enter an operation (ex: 2 + 2) : ").strip()
        list_operation = [element for element in operation_choice.split(" ")]
        if list_operation[0].isdigit() and list_operation[2].isdigit():
            resultat = calcul(int(list_operation[0]), list_operation[1], int(list_operation[2]))
            add_to_history(list_operation[0], list_operation[1], list_operation[2], resultat, historique)
            export_to_json(history, 'historique_calcul.json')
            print(f"\nThe result is {resultat}.")
        else:
            print("Please enter a valid operation (ex: 2 + 2).")
''' 
#Ce gros bloc sert uniquement à tester les trucs. Je le laisse pour que vous puissiez tester si vous voulez.

