class Library:
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor()

    def displayAvailableBooks(self):
        try:
            self.cursor.execute("SELECT Title FROM Books WHERE IsAvailable = 1")
            books = self.cursor.fetchall()
            print("Books present in this library are: ")
            for book in books:
                print(" *" + book[0])
        except Exception as e:
            print("Error fetching books. Please try again later.")
            print("Error details:", e)

    def borrowBook(self, bookName):
        try:
            self.cursor.execute("SELECT BookID FROM Books WHERE Title = ? AND IsAvailable = 1", (bookName,))
            book = self.cursor.fetchone()
            if book:
                self.cursor.execute("UPDATE Books SET IsAvailable = 0 WHERE BookID = ?", (book[0],))
                self.cursor.execute(
                    "INSERT INTO Transactions (BookID, BorrowerName) VALUES (?, ?)",
                    (book[0], "StudentName")  # Replace "StudentName" dynamically
                )
                self.conn.commit()
                print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days.")
            else:
                print("Sorry, this book is either not available or has already been issued to someone else.")
        except Exception as e:
            print("Error processing your request. Please try again later.")
            print("Error details:", e)

    def returnBook(self, bookName):
        try:
            self.cursor.execute("SELECT BookID FROM Books WHERE Title = ? AND IsAvailable = 0", (bookName,))
            book = self.cursor.fetchone()
            if book:
                self.cursor.execute("UPDATE Books SET IsAvailable = 1 WHERE BookID = ?", (book[0],))
                self.cursor.execute(
                    "UPDATE Transactions SET ReturnDate = GETDATE() WHERE BookID = ? AND ReturnDate IS NULL", (book[0],)
                )
                self.conn.commit()
                print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")
            else:
                print("This book was not borrowed or does not exist in the library.")
        except Exception as e:
            print("Error processing your return request. Please try again later.")
            print("Error details:", e)
