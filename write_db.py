import csv
import datetime
import os.path


def write_database(name, id_no, credit_card_no, credit_card_pass, description, total_cost):
    now = datetime.datetime.now()

    new_order = [name, id_no, credit_card_no, credit_card_pass, description, total_cost, now]
    file_exists = os.path.isfile("Orders_Database.csv")

    with open("Orders_Database.csv", "a") as file:
        writer = csv.writer(file)
        if file_exists:
            writer.writerow(new_order)
        else:
            headers = ["Name", "Id", "Card Number", "Card Password", "Description", "Total Price(TL)", "Order Time"]    #columns headers
            writer.writerow(headers)
            writer.writerow(new_order)
