import sys
import cx_Oracle
import string
import getpass

def connectToSQL(username, password):
    print("\nConnecting...")
    
    host = "@gwynne.cs.ualberta.ca:1521/CRS"
    connStr = username + "/" + password + host

    connection = cx_Oracle.connect(connStr)
    curs = connection.cursor()

    return 0

def login():
    print("User information")
    username = input("Username: ")
    password = getpass.getpass()
    
    return username, password


def main():
    username,password = login()
    connectToSQL(username, password)
    return 0

if __name__ == "__main__":
    main()