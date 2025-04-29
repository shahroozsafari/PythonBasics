
from os import system
from sys import path
clear = lambda : system("cls")


from json import load
try :
    with open(path[0]+"/books_database.json","r") as database :
        books = load(database)
except (FileNotFoundError) :
    books = []

def validate_isbn(isbn) :
    if len(isbn) != 5 :
        raise ValueError("ISBN must be 5 digit number")
    for book in books :
        if book["isbn"] == isbn :
            raise NameError("Duplicate value for ISBN !")
         
def add_book():
    clear()
    global books            # Optional Code
    book = {}
    book["title"] = input("Enter title of book : ")
    book["author"] = input("Enter author of book : ")
    while True:
        try :
            book["pages"] = int(input("Enter number of pages : "))
            book["price"] = float(input("Enter price of the book : "))
            book["year"] = int(input("Enter year of publish : ")) 
            break
        except (ValueError) :
            input("\nYou MUST enter a number. Try again ...")
    while True :
        try :          
            book["isbn"] = input("Enter ISBN : ")
            validate_isbn(book["isbn"])
            break 
        except (ValueError):
            input("Invalide ISBN for this book. Try again ...")
        except (NameError) :
            input("Duplicate value for ISBN !")
    books.append(book)
    input("\nThis book has been added to database successfully. Pree Enter to continue ...")

def list_books():
    clear()
    from tabulate import tabulate
    print(tabulate(books,headers="keys"))
    input("\nPress Enter to continue ...")
    # for book in books : 
    #     print("Title :",book["title"])
    #     print("Author :",book["author"]) 
    #     print("Pages :",book["pages"]) 
    #     print("Price :",book["price"])
    #     print("Year :",book["year"])
    #     print("ISBN :",book["isbn"]) 
    #     print(20*"-")
    

def find_book() :
    clear()
    isbn = input("Enter ISBN for search a book : ")
    for book in books :
        if book["isbn"] == isbn :
            print("Title :",book["title"])
            print("Author :",book["author"]) 
            print("Pages :",book["pages"]) 
            print("Price :",book["price"])
            print("Year :",book["year"])
            print("ISBN :",book["isbn"]) 
            print(20*"-")
            input("Press Enter to continue ...")
            break
    else :
        input("\nThis book doen't exist in books database ! press enter to return to menu.")

def delete_book() :
    clear()
    isbn = input("Enter ISBN for delete a book : ")
    for book in books :
        if book["isbn"] == isbn :
            books.remove(book)
            input("\nThis has been deleted successfully. Press Enter to continue.")
            break
    else :
        input("\nThis book doen't exist in books database ! press enter to return to menu.")

def save_json():
    from json import dump
    try :
        with open(path[0]+"/books_database.json","w") as database :
            dump(books,database,indent=4)
            input("\nBooks database has been saved !")
    except (PermissionError) :
        input("Save this file in diffrent location .")
        return False
    return True

def save_books() :
    import pickle
    with open(path[0]+"/books_database.info","wb") as database :
        pickle.dump(books,database)
        input("\nBooks database has been saved !")


def save_excel() :
    # import openpyxl as xl
    from openpyxl import Workbook
    excel_file = Workbook()
    sheet = excel_file.active
    sheet.title = "Books_data"

    for book in books :
        sheet.append(list(book.values()) )

    excel_file.save(path[0]+"/books_databse.xlsx")  

def save_pandas():
    import pandas as pd
    dataframe = pd.DataFrame(books)
    dataframe.to_excel(path[0]+"/books_databse2.xlsx",index=False)
