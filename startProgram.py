"""
Group members: 
    Steven Cherfan
    Kathleen Baker
    Brandon Smolley
"""

import sys
import cx_Oracle
import string
import random
import getpass
from prescribeTest import *
from enterTestResult import *
from searchPatient import *
from searchDoctor import *
from updatePatient import *
from alarmingPatient import *

def mainMenu(username):
    valid_input = ["exit", "1", "2", "3", "4", "5", "6"]
    print("This is the main menu, from here you can: ")
    print("1) Prescribe a test")
    print("2) Enter a test result")
    print("3) Update patient information")
    print("4) Search for a patient")
    print("5) Search for a doctor")
    print("6) Search for patients who have reached alarming age but haven't taken a type of test")
    print("Type 'exit' to close this application")

    result = ""
    while result not in valid_input:
        result = input("\nEnter task number: ")
        if result not in valid_input:
            print("  Please enter a valid command")

    return result


def connectToSQL(username, password):
    print("\nConnecting...")

    host = "@gwynne.cs.ualberta.ca:1521/CRS"
    connStr = username + "/" + password + host

    try:
        connection = cx_Oracle.connect(connStr)
        print("Connected!\n")
        curs = connection.cursor()
        print("Hello", username + "!\n")

    except cx_Oracle.DatabaseError as exc:
        error, = exc.args
        print("Oracle code:", error.code)
        print("Oracle message:", error.message)

    return connection, curs

def menuOptionSelected(result, connection, curs):
    if result == "exit":
        return

    elif int(result) == 1:
        prescribeTest(connection, curs)

    elif int(result) == 2:
        enterTestResult(connection, curs)

    elif int(result) == 3:
        updatePatient(connection, curs)

    elif int(result) == 4:
        searchPatient(connection, curs)

    elif int(result) == 5:
        searchDoctor(connection, curs)

    elif int(result) == 6:
        alarmingPatient(connection, curs)

def login():
    print("User information")
    username = input("Username: ")
    password = getpass.getpass() 
    return username, password


def main():  
    error = True
    i = 0
    while error == True:
        if i > 3:
            return
        try:
            username,password = login()
            connection, curs = connectToSQL(username, password)
            error = False
        except:
            print("Failed to connect, please try again\n")
            i += 1
    result = None
    id = generateId()
    while(result != "exit"):
        result = mainMenu(username)  
        menuOptionSelected(result, connection, curs)
    #print(result)  
    connection.close()
    #prescribeTest()
    print("\nConnection closed")

if __name__ == "__main__":
    main()
