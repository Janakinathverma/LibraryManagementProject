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

-- Add sample data
INSERT INTO Books (Title) VALUES 
('Algorithms'),
('Django'),
('Clrs'),
('Python Notes');
