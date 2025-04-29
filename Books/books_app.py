
# V 4.3.2

import books_operations as bo

#----------------------- UI ----------------------
while True :
    bo.clear()
    print(30*"=")
    print("Press A to add a book")
    print("Press L to list all books")
    print("Press F to find a book ")
    print("Press D to delete a book")
    print("Press S to save books")
    print("Press SE to save books in Excel file")
    print("Press Q to quit application")
    print(30*"=")
    choice = input("Enter your choice : ").upper()

    if choice == 'A'  :
        bo.add_book()
    elif choice == 'L'  :
        bo.list_books()
    elif choice == 'F' :
        bo.find_book()
    elif choice == 'D' :
        bo.delete_book()
    elif choice == 'S' :
        bo.save_json()
    elif choice == 'SE' :
        bo.save_pandas()
    elif choice == 'Q' :
        break
    else :
        input("Wrong choice ! Try again ...")
