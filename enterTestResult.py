import cx_Oracle
from prescribeTest import getTestId
"""
 Medical Test
 
This program handles entering a test result to the data base.
This program is used by medical lab personnel to enter the test result after a medical test is completed.

Your program shall allow the user to enter all necessary information to complete this task,
including, but not limiting to, the lab name, test date, and of course, the test result.

No lab shall conduct a test on a patient without a proper prescription.
Therefore, the program shall first ask the user to enter the necessary information,
such as the name or health care number of the patient, the name of the doctor who prescribes the test,
or any other information, to search the database for a proper test record.

The request will be rejected if a proper test record cannot be located in the database.

"""

def enterTestResult(connection, curs):
    print("Search for an existing prescription and then enter new information to record.")
    print("Please enter search information")
    testID = findTestRecord(connection, curs)
    print("Please enter prompted information, if information is unknown or unavailable leave blank " +
          "by pressing enter.")
    
    while(1):
        typeID = input("Enter test type name: ")
        if typeID != "":
            typeID = getTestId(typeID, curs)
            try:
                query = "UPDATE test_record set type_id=" + str(typeID) + " "
                query += "WHERE test_id = '" + testID + "'"
                curs.execute(query)
                break
            except cx_Oracle.DatabaseError as exc:
                error, = exc.args
                print("Oracle code:", error.code)
                print("Oracle message:", error.message)
                print("Enter a proper test ID.")
        else:
            break
   
    while(1):
        testResult = input("Enter a test result: ")
        if testResult != "":
            try:
                query = "UPDATE test_record set result='" + testResult + "' "
                query += "WHERE test_id = '" + testID + "'"
                curs.execute(query)
                break
            except cx_Oracle.DatabaseError as exc:
                error, = exc.args
                print("Oracle code:", error.code)
                print("Oracle message:", error.message)
        else:
            break
    while(1):
        prescribeDate = input("Enter the test's prescribed date(YYYY-MM-DD): ")        
        if prescribeDate != "":
            try:
                query = "UPDATE test_record set prescribe_date=to_date('" + prescribeDate + "','YYYY-MM-DD') "
                query += "WHERE test_id = '" + testID + "'"
                curs.execute(query)
                break
            except cx_Oracle.DatabaseError as exc:
                error, = exc.args
                print("Oracle code:", error.code)
                print("Oracle message:", error.message)
                print("Enter a proper prescribe date.")
        else:
            break
    while(1):
        testDate = input("Enter the date when the test took place(YYYY-MM-DD): ")
        if testDate != "":
            try:
                query = "UPDATE test_record set test_date=to_date('" + testDate + "','YYYY-MM-DD') "
                query += "WHERE test_id = '" + testID + "'"
                curs.execute(query)
                break
            except cx_Oracle.DatabaseError as exc:
                error, = exc.args
                print("Oracle code:", error.code)
                print("Oracle message:", error.message)
                print("Enter a proper test date.")
        else:
            break
    try:
        query = "commit"
        curs.execute(query)
    except cx_Oracle.DatabaseError as exc:
        error, = exc.args
        print("Oracle code:", error.code)
        print("Oracle message:", error.message)

    print()
    print("Entry successful.")
    print()
        
def findTestRecord(connection, curs):
    print("If the test ID is known then leave the other fields blank and fill in the known test ID.")
    print("Other wise fill in known fields and use the printed list to enter the test ID when prompted.")
    i = 0
    while(1):
        if i == 0 or i == 2:
            print("Please fill in at least one of the fields, press enter to leave blank.")
            name = input("Enter a name of a patient: ")
            testID = input("Enter a test ID number: ")
            healthCareNo = input("Enter a health care number of a patient: ")
            employeeNo = input("Enter a doctor employee number: ")
        else:
            print("Please enter desired test_id from list of records. Or leave it blank to search again.")

            while(1):
                testID = input("Enter a test ID number: ")
                if testID.isdigit() == True:
                    break
                else:
                    print("Please enter an integer")
            if testID == "":
                i = 1
        if testID == "":
            try:
                query = "SELECT r.* "
                query += "FROM test_record r, patient p "
                query += "WHERE r.patient_no = p.health_care_no AND "
                query += "p.name = '" + name + "'"
                curs.execute(query)
                resultName = curs.fetchall()
            except cx_Oracle.DatabaseError as exc:
                error, = exc.args
                print("Oracle code:", error.code)
                print("Oracle message:", error.message)
                
            try:
                query = "SELECT r.* "
                query += "FROM test_record r, patient p "
                query += "WHERE r.patient_no = p.health_care_no AND "
                query += "r.patient_no = '" + healthCareNo + "'"
                curs.execute(query)
                resultHCN = curs.fetchall()
            except cx_Oracle.DatabaseError as exc:
                error, = exc.args
                print("Oracle code:", error.code)
                print("Oracle message:", error.message)
        
            try:
                query = "SELECT r.* "
                query += "FROM test_record r, patient p "
                query += "WHERE r.patient_no = p.health_care_no AND "
                query += "r.employee_no = '" + employeeNo + "'"
                curs.execute(query)
                resultEN = curs.fetchall()
            except cx_Oracle.DatabaseError as exc:
                error, = exc.args
                print("Oracle code:", error.code)
                print("Oracle message:", error.message)
            if resultName == [] and resultHCN == [] and resultEN == []:
                print("Query not found.\n")
                i = 2
            else:
                for res in resultName, resultHCN, resultEN:
                    for i in res:
                        output = "Test ID: " + str(i[0]) + "\n"
                        output += "Test type ID: " + str(i[1]) + "\n"
                        output += "Patient number: " + str(i[2]) + "\n"
                        output += "Employee Number: " + str(i[3]) + "\n"
                        output += "Medical lab: " + i[4] + "\n"
                        output += "Test result: " + i[5] + "\n"
                        output += "Prescribe date: " + str(i[6]) + "\n"
                        output += "Test date: " + str(i[7]) + "\n"

                print(output)
                
            if i == 0:
                i = 1
            else:
                i = 0
        elif testID != "":
            try:
                query = "SELECT r.* "
                query += "FROM test_record r "
                query += "WHERE r.test_id = '" + testID + "'"
                curs.execute(query)
                result = curs.fetchall()
            except cx_Oracle.DatabaseError as exc:
                error, = exc.args
                print("Oracle code:", error.code)
                print("Oracle message:", error.message)
            if result == []:
                print("Query not found.\n")
            else:
                for res in result:
                    output = "Test ID: " + str(res[0]) + "\n"
                    output += "Test type ID: " + str(res[1]) + "\n"
                    output += "Patient number: " + str(res[2]) + "\n"
                    output += "Employee Number: " + str(res[3]) + "\n"
                    output += "Medical lab: " + res[4] + "\n"
                    output += "Test result: " + res[5] + "\n"
                    output += "Prescribe date: " + str(res[6]) + "\n"
                    output += "Test date: " + str(res[7]) + "\n"

                print(output)
                return testID
