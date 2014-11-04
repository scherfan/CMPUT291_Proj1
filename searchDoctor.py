"""
Doctor Search
This program handles the querying search for doctors and their information
stored in the database.
"""

def searchDoctor(connection, curs):
    docID = ""
    docNum = None
    print("Search for information of all tests prescribed by a given doctor"
         " during a specific time period.")
    while(1):
        docID = input("Enter a name or employee number: ")
        if docID.isdigit() == True:
            docNum = int(docID)
            break
        elif docID.isalnum() == False and docID.isdigit() == False:
            break
        else:
            print("Please enter a valid field.")

    dateStart = ""
    dateEnd = ""
    while(1):
        dateStart = input("Enter a start date(yyyy-mm-dd):")
        if (dateStart[:4].isdigit() == True and dateStart[4] == '-'
            and dateStart[5:7].isdigit() == True and dateStart[7] == '-'
            and dateStart[8:10].isdigit() == True):
            break
        else:
            print("Please enter a valid field.")
    while(1):
        dateEnd = input("Enter an end date(yyyy-mm-dd):")
        if (dateEnd[:4].isdigit() == True and dateEnd[4] == '-'
            and dateEnd[5:7].isdigit() == True and dateEnd[7] == '-'
            and dateEnd[8:10].isdigit() == True):
            break
        else:
            print("Please enter a valid field.")

    if docID != "":
        print(docID)
        print(dateStart)
        print(dateEnd)
    else:
        print(docNum)
        print(dateStart)
        print(dateEnd)
