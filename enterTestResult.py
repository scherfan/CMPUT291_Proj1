import cx_Oracle
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
    findTestRecord(connection, curs)
        



def findTestRecord(connection, curs):
    print("Please fill in at least one of the fields, press enter to leave blank.")
    name = input("Enter a name of a patient: ")
    testID = input("Enter a test ID number: ")
    healthCareNo = input("Enter a health care number of a patient: ")
    employeeNo = input("Enter a doctor employee number: ")
    
    try:
        query = "SELECT r.* "
        query += "FROM test_record r, patient p "
        query += "WHERE r.patient_no = p.health_care_no AND "
        query += "p.name = '" + name + "'"
        curs.execute(query)
        result = curs.fetchall()
    except cx_Oracle.DatabaseError as exc:
        error, = exc.args
        print("Oracle code:", error.code)
        print("Oracle message:", error.message)

    if result == []:
        print("Query not found.")
        return
    for res in result:
        print(res)
