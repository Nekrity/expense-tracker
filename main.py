#   _____                                       _____               _             
#  | ____|_  ___ __   ___ _ __  ___  ___  ___  |_   _| __ __ _  ___| | _____ _ __ 
#  |  _| \ \/ / '_ \ / _ \ '_ \/ __|/ _ \/ __|   | || '__/ _` |/ __| |/ / _ \ '__|
#  | |___ >  <| |_) |  __/ | | \__ \  __/\__ \   | || | | (_| | (__|   <  __/ |   
#  |_____/_/\_\ .__/ \___|_| |_|___/\___||___/   |_||_|  \__,_|\___|_|\_\___|_|   
#             |_|                                                                 

#
# Uzdevums:
# Uzrakstīt programmu, kas ļauj
# - ievadīt izdevumus: nosaukumu, summu un kategoriju
# - atspoguļot uz ekrāna visus izdevumus
# - iespēja atlasīt 10 lielākus izdevumus
# - iespēja atlasīt 10 mazākus izdevumus
# - iespēja apskatīt vidējo izdevumu summu
# [!] Programmai jaglabā izdevumu stāvokli kad programma ir izslēgta palaista no jauna
#
import json


expenses_file = open('expenses.json') # opening JSON file
expenses = json.load(expenses_file) # returns JSON object as a dictionary
expenses_file.close()


# load expenses from expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Python read JSON file)
expenses_comparison=expenses.copy()
def sort_expenses(expenses_comparison):
    return int(expenses_comparison["sum"])

while True:
    command = input("\nChoose command:")
    if command == "1":
        expenses_write={}
        expenses_write["name"]=input("write expenses name: ")
        expenses_write["sum"]=int(input("write sum of expenses: "))
        expenses_write["category"]=input("write category of expenses: ")
        expenses.append(expenses_write)
        print(expenses)
        pass
    if command == "2":
        print(expenses)
        pass
    if command == "3":
        expenses_comparison.sort(key=sort_expenses, reverse=True)
        print(expenses_comparison[0:10])
        pass
    if command == "4":
        expenses_comparison.sort(key=sort_expenses)
        print(expenses_comparison[0:10])
        pass
    if command == "5":
        print("average expenses: ",average)
    if command == "e":
        with open("expenses.json", "w") as outfile:
            json.dump(expenses, outfile)
        print("Exiting...")
        break

# save expenses to expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Writing JSON to a file in Python)
pass

