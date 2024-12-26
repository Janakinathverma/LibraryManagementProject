import pyodbc

def connect_to_db():
    try:
        conn = pyodbc.connect('DRIVER={SQL Server};'
                              'SERVER=YourServerName;'
                              'DATABASE=LibraryDB;'
                              'Trusted_Connection=yes;')
        return conn
    except pyodbc.Error as e:
        print("Error connecting to the database. Please check your configuration.")
        print("Error details:", e)
        return None
