"""
Group members: 
    Steven Cherfan
    Kathleen Baker
    Brandon Smolley
"""

import sys
import cx_Oracle
import string
import getpass
from prescribeTest import *


def mainMenu(username):
    valid_input = ["exit", "1", "2", "3", "4", "5", "6"]
    print("Hello", username + "!\n")
    print("This is the main menu, from here you can: ")
    print("1) Prescribe a test")
    print("2) Enter a test result")
    print("3) Update patient information")
    print("4) Search for a patient")
    print("5) Search for a doctor")
    print("6) Search for patients who haven't taken important tests")
    print("Type 'exit' to close this application")

    result = ""
    while result not in valid_input:
        result = input("\nEnter task number: ")
        if result not in valid_input:
            print("Please enter a valid command")

    return result


def connectToSQL(username, password):
    print("\nConnecting...")

    host = "@gwynne.cs.ualberta.ca:1521/CRS"
    connStr = username + "/" + password + host

    try:
        connection = cx_Oracle.connect(connStr)
        print("Connected!")
        curs = connection.cursor()

    except cx_Oracle.DatabaseError as exc:
        error, = exc.args
        print( sys.stderr, "Oracle code:", error.code)
        print( sys.stderr, "Oracle message:", error.message)

    return connection

def menuOptionSelected(result):
    if result == "exit":
        return

    elif int(result) == 1:
        # Call prescribeTest()
        prescribeTest()
        #print(int(result))

    elif int(result) == 2:
        # Call enterTestResult()
        print(int(result))

    elif int(result) == 3:
        # Call updatePatient()
        print(int(result))

    elif int(result) == 4:
        # Call searchPatient()
        print(int(result))

    elif int(result) == 5:
        # Call searchDoctor()
        print(int(result))

    elif int(result) == 6:
        # Call alarmingPatient()
        print(int(result))


    return


def login():
    print("User information")
    username = input("Username: ")
    password = getpass.getpass()   
    return username, password


def main():
    username,password = login()
    connection = connectToSQL(username, password)
    result = mainMenu(username)  
    menuOptionSelected(result)
    #print(result)  
    connection.close()
    #prescribeTest()
    print("\nConnection closed")

if __name__ == "__main__":
    main()
