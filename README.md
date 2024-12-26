# Library Management System with SQL Integration

## **Overview**
The Library Management System is a Python-based application that allows users to interact with a library's book inventory. The project integrates with Microsoft SQL Server to manage book records, transactions, and borrowing history. This system is designed for ease of use, modularity, and scalability.

---

## **Features**
1. **List Available Books**: Displays all books currently available in the library.
2. **Borrow Books**: Allows users to borrow a book from the library, updating the database.
3. **Return Books**: Enables users to return a borrowed book, marking it as available again in the database.
4. **Error Handling**: Robust error handling to manage database connection issues, invalid user inputs, and unexpected errors.

---

## **Technologies Used**
- **Python**: Core programming language.
- **Microsoft SQL Server**: Backend database to store and manage book data.
- **pyodbc**: Python library to connect and interact with the SQL database.

---

## **Project Structure**
```plaintext
LibraryManagement/
│
├── main.py                # Main script to run the application
├── database/
│   ├── setup.sql          # SQL script to create and populate the database
├── lib/
│   ├── library.py         # Library class to manage book operations
│   ├── student.py         # Student class to handle user interactions
│   ├── db_connection.py   # Database connection logic
│
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
└── .gitignore             # Files and directories to be ignored by git
```

---

## **Setup Instructions**

### **1. Prerequisites**
- Python 3.8 or later
- Microsoft SQL Server installed and configured
- Python library dependencies (listed in `requirements.txt`)

### **2. Database Setup**
1. Open the SQL Server Management Studio.
2. Run the `database/setup.sql` script to create the database and tables, and populate initial data.

```sql
CREATE DATABASE LibraryDB;
USE LibraryDB;

CREATE TABLE Books (
    BookID INT PRIMARY KEY IDENTITY(1,1),
    Title NVARCHAR(100) NOT NULL,
    IsAvailable BIT DEFAULT 1
);

CREATE TABLE Transactions (
    TransactionID INT PRIMARY KEY IDENTITY(1,1),
    BookID INT,
    BorrowerName NVARCHAR(100),
    BorrowDate DATETIME DEFAULT GETDATE(),
    ReturnDate DATETIME,
    FOREIGN KEY (BookID) REFERENCES Books(BookID)
);

INSERT INTO Books (Title) VALUES
('Algorithms'),
('Django'),
('Clrs'),
('Python Notes');
```

### **3. Install Dependencies**
Install required Python libraries:
```bash
pip install -r requirements.txt
```

### **4. Configure Database Connection**
Edit `lib/db_connection.py` and replace `YourServerName` with your SQL Server instance name:
```python
conn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=YourServerName;'
                      'DATABASE=LibraryDB;'
                      'Trusted_Connection=yes;')
```

---

## **Usage**
Run the application using:
```bash
python main.py
```
You will see the following menu:
```
 ====== Welcome to Central Library ======
 Please choose an option:
 1. List all the books
 2. Request a book
 3. Add/Return a book
 4. Exit the Library
```

### **Example Workflow**
1. **List Books**: Choose option `1` to display available books.
2. **Borrow a Book**: Choose option `2` and enter the book name.
3. **Return a Book**: Choose option `3` and enter the book name.
4. **Exit**: Choose option `4` to exit the system.

---

## **Error Handling**
- **Database Connection Issues**: Displays an error message if the connection to the database fails.
- **Invalid Inputs**: Handles incorrect menu choices and provides user-friendly feedback.
- **Unexpected Errors**: Catches and displays error details for debugging purposes.

---

## **Future Enhancements**
1. Add a web interface using Flask or Django.
2. Implement user authentication and authorization.
3. Include book search functionality.
4. Add support for fine calculation for overdue books.
5. Introduce logging to track system activities.

---

## **Contact**
For any queries or contributions, please reach out at: janakinathv@gmail.com

