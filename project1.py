import sys
import cx_Oracle

def connectToSQL(username, password):
    print("\nConnecting...")
    print(username, password)
    connStr = username + "/" + password
    connStr = 'username/password@host'
    return 

def login():
    print("User information")
    username = input("Enter a username: ")
    password = input("Enter a password: ") 
    return username, password


def main():
    username,password = login()
    connectToSQL(username, password)
    return 0

if __name__ == "__main__":
    main()