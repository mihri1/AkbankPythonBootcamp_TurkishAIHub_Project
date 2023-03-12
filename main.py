from choices import Pizza, Classic, Margherita, Turkish, Italiano, Olive, Mushroom, Bacon, Cheese, Corn
from write_db import write_database


def main():
    f = open("Menu.txt", "r")
    print(f.read())

    pizza_choice = input("Please choice a pizza 1, 2, 3, 4 : ")

    if pizza_choice == "1":
        pizza = Classic()
    elif pizza_choice == "2":
        pizza = Margherita()
    elif pizza_choice == "3":
        pizza = Turkish()
    else:
        pizza = Italiano()

    sauce_choice = input("Please choice a sauce for pizza 12, 13, 14, 16 : ")

    if sauce_choice == "11":
        sos = Olive()
    elif sauce_choice == "12":
        sos = Mushroom()
    elif sauce_choice == "13":
        sos = Cheese()
    elif sauce_choice == "14":
        sos = Bacon()
    else:
        sos = Corn()

    print("Selected pizza: ", pizza.name, ": ", pizza.description)
    print("Selected sauce: ", sos.description)
    print("Total Cost: ", int(pizza.cost + sos.cost), " TL")

    print("----Please enter your information for ending...")
    name = input("Name: ")
    id_no = input("Citizen identity: ")
    credit_card_no = input("Credit card number: ")
    credit_card_pass = input("Credit card password:")
    description = pizza.name + " " + pizza.description + " : " + sos.description
    total_cost = int(pizza.cost + sos.cost)

    write_database(name, id_no, credit_card_no, credit_card_pass, description, total_cost)


main()
