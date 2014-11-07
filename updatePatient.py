import cx_Oracle
import datetime

def updatePatient(connection, curs):
    while(True):
        patient_id = input("\nEnter patient health care number: ")
        try:
            query = "SELECT * FROM patient WHERE health_care_no = " + patient_id
            curs.execute(query)
            result = curs.fetchall()
            #patient not in table yet
            if len(result) == 0:
                newPatient(connection, curs, patient_id)
                addTestNotAllowed(connection, curs, patient_id)
                break
                return  
            else:
                print("\nPatient selected:")
                print("Health care number: "+str(result[0][0]))
                print("Name: "+result[0][1])
                if result[0][2] != None:
                    print("Address: "+result[0][2])
                if str(result[0][3]) != None:
                    print("Birth date: "+str(result[0][3])[:10])
                if result[0][4] != None:
                    print("Phone number: "+result[0][4])

                oldPatient(connection, curs, patient_id)
                updateTestNotAllowed(connection, curs, patient_id)
                break
                return
        except:
            print("\nError finding patient health care number - must be an integer.\n")

# for patients who are already in system
def updateTestNotAllowed(connection, curs, patient_id):
    print("Current test(s) not allowed for patient: ")
    # print tests currently not allowed - do I need this?
    query = """SELECT t.test_name
FROM patient p, test_type t, not_allowed n
WHERE t.type_id = n.type_id AND
      p.health_care_no = n.health_care_no AND
      p.health_care_no = """+patient_id
    try:
        curs.execute(query)
        tests = curs.fetchall()
        #print(tests)
        i= 0
        if len(tests) == 0:
            print("None")
        while i < len(tests):
            print(tests[i][0])
            i += 1
    except cx_Oracle.DatabaseError as ex:
        error, = ex.args
        print("Error message ="+str(error.message))

    addTestNotAllowed(connection, curs, patient_id)
    return

def addTestNotAllowed(connection, curs, patient_id):
    # patient is new
    while(True):
        test = input("\nEnter a test the patient is not allowed to take or press enter to skip: ")
        # enter skips
        if test != '':
            query = "SELECT type_id FROM test_type WHERE test_name = '"+test+"'"
            try:
                curs.execute(query)
                test_id = curs.fetchall()
                if len(test_id) == 0:
                    # test doesn't exist - ask again
                    print("Test doesn't exist.")
                else:
                    type_id = test_id[0][0]
                    query2 = "insert into not_allowed values("+patient_id+", "+str(type_id)+")"
                    try:
                        curs.execute(query2)
                        connection.commit()
                    except cx_Oracle.DatabaseError as ex:
                        error, = ex.args
                        print("Error message ="+str(error.message))
                        print("Error adding test not allowed.")
            except cx_Oracle.DatabaseError as ex:
                error, = ex.args
                print("Error message ="+str(error.message))
        elif test == '':
            break
    return

def newPatient(connection, curs, patient_id):
    print("Patient doesn't exist - insert new patient.\n")
    name = input("Enter patient name: ")
    while name == '':
        print("Patient name cannot be empty.")
        name = input("Enter patient name: ")
    address = input("Enter patient's address: ")
    birth = input("Enter patient's birth date in YYYY-MM-DD format: ")
    result = validate(birth)
    while result == False:
        birth = input("Enter patient's birth date in YYYY-MM-DD format: ")
        result = validate(birth)
    phone = input("Enter patient's phone number: ")
    patient = (patient_id, name, address, birth, phone)
    query = "INSERT INTO patient values ("+patient_id+", '"+name+"', '"+address+"', date '"+birth+"', '"+phone+"')"
    try:
        curs.execute(query)
        connection.commit()
        print("Patient added.\n") # print what was added
    except:
        print("Error inserting patient.")
    return

def oldPatient(connection, curs, patient_id):
    #can update patient info - ask which info
    print("\nUpdate patient info - enter new info or press enter to skip.")
    name = input("Enter patient name: ")
    if name != "":
        try:
            # works: needs '' around name
            query = "UPDATE patient set name = '"+name+"' where health_care_no = "+patient_id
            curs.execute(query)
            connection.commit()
        except:
            print("Error updating name - maximum length is 100 characters.")
    address = input("Enter patient's address: ")
    if address != '':
        try:
            query = "UPDATE patient set address = '"+address+"' where health_care_no = "+patient_id
            curs.execute(query)
            connection.commit()
        except:
            print("Error updating address - maximum length is 200 characters.")
    birth = input("Enter patient's birth date in YYYY-MM-DD format: ")
    if birth != '':
        try:
            result = validate(birth)
            while result == False and birth != '':
                birth = input("Enter patient's birth date in YYYY-MM-DD format: ")
                if birth != '':
                    result = validate(birth)
            if birth != '':
                query = "UPDATE patient set birth_day = date '"+birth+"' where health_care_no = "+patient_id
                curs.execute(query)
                connection.commit()
        except:
            print("Error updating birth date - must be in YYYY-MM-DD format.")
    phone = input("Enter patient's phone number: ")
    if phone != '':
        try:
            query = "UPDATE patient set phone = '"+phone+"' where health_care_no = "+patient_id
            curs.execute(query)
            connection.commit()
        except:
            print("Error updating phone - maximum length is 10 digits.")
    print("Patient info updated.\n")
    return

def validate(birth):
    try:
        datetime.datetime.strptime(birth, "%Y-%m-%d")
        return True
    except:
        print("Must be valid date in format YYYY-MM-DD.")
        return False
