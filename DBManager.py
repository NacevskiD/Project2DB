import Database

def menu():
    print("\n1. Create\n2. Add\n3. Update\n4. Delete\n5. Display all\n6. Display single\n7. Exit")

menu()
choice = int(input())

db = Database.myDB()


while choice != 7:

    if choice == 1:
        db.createTable()
        menu()
        choice = int(input())
    elif choice == 2:
        firstName = input("Enter the first name:\n")
        lastName = input("Enter the last name:\n")
        employed = input("Employment? y/n:\n")
        phone = input("Phone number\n")
        salary = input("Salary\n")
        date = input("Enter date YYYY-MM-DD")
        if employed == "y" or employed == "Y":
            employed = True
        else:
            employed = False
        db.addItem(firstName,lastName,employed,int(phone),float(salary),date)
        print("Item added")
        menu()
        choice = int(input())
    elif choice == 3:
        id = input("Enter the id of the item you want changed")
        db.showSingle(id)
        firstName = input("Enter the first name:\n")
        lastName = input("Enter the last name:\n")
        employed = input("Employment? y/n:\n")
        phone = input("Phone number\n")
        salary = input("Salary\n")
        date = input("Enter date YYYY-MM-DD")
        if employed == "y" or employed == "Y":
            employed = True
        else:
            employed = False
        db.alterDatabase(id,firstName,lastName,employed,int(phone),float(salary),date)
        print("Item changed")
        menu()
        choice = int(input())

    elif choice == 4:
        id = input("Enter the id of the item to delete:\n")
        db.deleteItem(int(id))
        menu()
        choice = int(input())
    elif choice == 5:
        db.showAll()
        menu()
        choice = int(input())
    elif choice == 6:
        id = input("Enter the id of the item you want to see\n")
        db.showSingle(id)
        menu()
        choice = int(input())


db.closeConnection()
