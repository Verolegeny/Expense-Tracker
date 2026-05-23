expenses = []

print("Welcome!")
print()
try:
    budget = int(input("What is your monthly budget?($) "))
except:
    print("Okay, that's enough.")
    exit()

while True:
    print()
    print("1. Add expense")
    print("2. View expenses")
    print("3. Exit")
    print("4. Delete Expense")
    print()


    option = int(input("Please select an option: "))
    if option == 1:
        print()
        category = (input("category(Food, Transport, Entertainment, Bills, Other): "))

        item = (input("item: "))
        
        try:
            amount = float(input("amount($): "))
        except:
            print("In numbers please!!!")
            continue

        print()


        expense = {"category": category, 
            "item": item, 
            "amount": amount
        }

        expenses.append(expense)

    elif option == 2:
        for expense in expenses:
            print()
            print("Category:", expense["category"])
            print("Item:", expense["item"])
            print("Amount:", expense["amount"],"$")
            print()

        spent = 0

        for expense in expenses:
            spent += expense["amount"]
        print("Total spent:", spent,"$")
        print()
        category1 = 0
        category2 = 0
        category3 = 0
        category4 = 0
        category5 = 0
        category6 = 0
        for expense in expenses:
            if expense["category"] == "Food":
                category1 += expense["amount"]
            elif expense["category"] == "Transport":
                category2 += expense["amount"]
            elif expense["category"] == "Entertainment":
                category3 += expense["amount"]
            elif expense["category"] == "Bills":
                category4 += expense["amount"]
            elif expense["category"] == "Other":
                category5 += expense["amount"]
            else:
                category6 += expense["amount"]
        print("Food: ", category1, "$")
        print()
        print("Transport: ", category2, "$")
        print()
        print("Entertainment: ", category3, "$")
        print()
        print("Bills: ", category4, "$")
        print()
        print("Other: ", category5, "$")
        print()
        print("Your category: ", category6, "$")
        print()
        biggest = 0
        for expense in expenses:
            if expense["amount"] > biggest:
                biggest = expense["amount"]
        if expense["amount"] == biggest:
            print("Biggest expense: ", expense["item"], "-", expense["amount"], "$")
            print()
        print("Highest paid: ", biggest, "$")
        print()
        if spent >= budget:
            print("You have spent too much money this month, cutie!")
        elif spent < budget:
            remains = budget - spent
            print("Remaining budget: ", remains, "$")
        

    
    elif option == 3:
        break

    elif option == 4:
        print()
        for index, expense in enumerate(expenses):
            print(index,":", expense["category"], "-", expense["item"], "-", expense["amount"],"$")
        print()
        choice = int(input("Which expense do you want to delete? "))
        if choice > len(expenses):
            print("Wrong!")
        expenses.pop(choice)
        print("Choice deleted")
    
    else:
        print()
        print("Oh come on! You can do it!")
        print()

        











