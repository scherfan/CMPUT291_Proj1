import sys
import cx_Oracle
import string
import getpass

def mainMenu(username):
    print("Hello", username + "!\n")
    print("This is the main menu, from here you can: ")
    print("1) Prescribe a test")
    print("2) Enter a test result")
    print("3) Update patient information")
    print("4) Search for a patient")
    print("5) Search for a doctor")
    print("6) Search for patients who haven't taken important tests")
    print("Type 'exit' to close this application")

    result = input("Enter task number: ")

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
        print(int(result))
        return
    elif int(result) == 2:
        # Call enterTestResult()
        print(int(result))
        return
    elif int(result) == 3:
        # Call updatePatient()
        print(int(result))
        return
    elif int(result) == 4:
        # Call searchPatient()
        print(int(result))
        return
    elif int(result) == 5:
        # Call searchDoctor()
        print(int(result))
        return
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
    print("Connection closed")

if __name__ == "__main__":
    main()
