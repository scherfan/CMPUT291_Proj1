"""
Doctor Search
This program handles the querying search for doctors and their information
stored in the database.
"""

def searchDoctor(connection, curs):
    docID = ""
    docNum = None
    print("Search for information of all tests prescribed by a given doctor")
    print("during a specific time period." + '\n')
    while(1):
        docID = input("Enter a name or employee number: ")
        if docID.isdigit() == True:
            docNum = int(docID)
            print('\n')
            break
        elif docID.isalnum() == False and docID.isdigit() == False:
            print('\n')
            break
        else:
            print("Please enter a valid field.\n")

    timePeriod = ""
    while(1):
        timePeriod = input("Enter a time interval(yyyy-mm-dd yyy-mm-dd):")
        if timePeriod.count(' ') == 1:
            timePeriod = timePeriod.split()
            print('\n')
            break
        else:
            print("Please enter a valid field.\n")

            if docID != "":
                print(docID)
                print('\n')
            else:
                print(docNum)
                print(timePeriod)
