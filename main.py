from lib.library import Library
from lib.student import Student
from lib.db_connection import connect_to_db

if __name__ == "__main__":
    conn = connect_to_db()
    if not conn:
        print("Exiting the program due to database connection error.")
        exit()

    centraLibrary = Library(conn)
    student = Student()

    while True:
        try:
            welcomeMsg = '''\n ====== Welcome to Central Library ======
            Please choose an option:
            1. List all the books
            2. Request a book
            3. Add/Return a book
            4. Exit the Library
            '''
            print(welcomeMsg)
            choice = int(input("Enter a choice: "))
            if choice == 1:
                centraLibrary.displayAvailableBooks()
            elif choice == 2:
                centraLibrary.borrowBook(student.requestBook())
            elif choice == 3:
                centraLibrary.returnBook(student.returnBook())
            elif choice == 4:
                print("Thanks for choosing Central Library. Have a great day ahead!")
                break
            else:
                print("Invalid Choice! Please enter a valid option.")
        except ValueError:
            print("Invalid input! Please enter a number corresponding to the menu options.")
        except Exception as e:
            print("An unexpected error occurred. Please try again.")
            print("Error details:", e)
