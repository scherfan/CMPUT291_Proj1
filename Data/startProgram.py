import sys
import cx_Oracle
import string
import getpass

def connectToSQL(username, password):
    print("\nConnecting...")

    host = "@gwynne.cs.ualberta.ca:1521/CRS"
    connStr = username + "/" + password + host

    try:
        connection = cx_Oracle.connect(connStr)
        print("Connected!")
        curs = connection.cursor()
        connection.close()

    except cx_Oracle.DatabaseError as exc:
        error, = exc.args
        print( sys.stderr, "Oracle code:", error.code)
        print( sys.stderr, "Oracle message:", error.message)

    print("Connection closed")


def login():
    print("User information")
    username = input("Username: ")
    password = getpass.getpass()   
    return username, password


def main():
    username,password = login()
    connectToSQL(username, password)

if __name__ == "__main__":
    main()
