"""
Doctor Search
This program handles the querying search for doctors and their information
stored in the database.
"""
import cx_Oracle
def searchDoctor(connection, curs):
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

    while(1):
        dateStart = input("Enter a start date(yyyy-mm-dd):")
        if (dateStart[:4].isdigit() == True and dateStart[4] == '-'
            and dateStart[5:7].isdigit() == True and int(dateStart[5:7]) > 0
            and int(dateStart[5:7]) < 32 and dateStart[7] == '-'
            and dateStart[8:10].isdigit() == True and int(dateStart[5:7]) < 13 and int(dateStart[5:7]) > 0):
            break
        else:
            print("Please enter a valid date.")
    while(1):
        dateEnd = input("Enter an end date(yyyy-mm-dd):")
        if (dateEnd[:4].isdigit() == True and dateEnd[4] == '-'
            and dateEnd[5:7].isdigit() == True and int(dateEnd[5:7]) > 0
            and int(dateEnd[5:7]) < 32 and dateEnd[7] == '-'
            and dateEnd[8:10].isdigit() == True and int(dateEnd[5:7]) < 13 and int(dateEnd[5:7]) > 0):
            break
        else:
            print("Please enter a valid date.")

    if docID != None:
        print("Search By:")
        print("Doctor's Name: " + docID)
        print("Start date: " + dateStart)
        print("End Date: " + dateEnd)

        try:
            query = "SELECT d.employee_no "
            query += "FROM doctor d, patient p "
            query += "WHERE d.health_care_no = p.health_care_no AND "
            query += "p.name = '" + docID + "'"

            curs.execute(query)
            result = curs.fetchall()
            result = result[0][0]

            query = "SELECT p.health_care_no, p.name, t.test_name, r.prescribe_date "
            query += "FROM patient p, test_type t, test_record r "
            query += "WHERE p.health_care_no = r.patient_no AND "
            query += "r.type_id = t.type_id AND "
            query += "r.employee_no = '" + str(result) + "' AND "
            query += "r.prescribe_date BETWEEN to_date('" + dateStart + "','YYYY-MM-DD') AND "
            query += "to_date('" + dateEnd + "', 'YYYY-MM-DD')"

            curs.execute(query)
            result = curs.fetchall()
            for res in result:
                print(res)
        except cx_Oracle.DatabaseError as exc:
            error, = exc.args
            print("Oracle code:", error.code)
            print("Oracle message:", error.message)
    else:
        print("Search By:")
        print("Doctor's Employee Number: " + docNum)
        print("Start date: " + dateStart)
        print("End Date: " + dateEnd)

        try:
            query = "SELECT p.health_care_no, p.name, t.test_name, r.prescribe_date "
            query += "FROM patient p, test_type t, test_record r "
            query += "WHERE p.health_care_no = r.patient_no AND "
            query += "r.type_id = t.type_id AND "
            query += "r.employee_no = '" + str(docNum) + "' AND "
            query += "r.prescribe_date BETWEEN to_date('" + dateStart + "','YYYY-MM-DD') AND "
            query += "to_date('" + dateEnd + "', 'YYYY-MM-DD')"

            curs.execute(query)
            result = curs.fetchall()
            for res in result:
                print(res)
        except cx_Oracle.DatabaseError as exc:
            error, = exc.args
            print("Oracle code:", error.code)
            print("Oracle message:", error.message)

        
    print()
