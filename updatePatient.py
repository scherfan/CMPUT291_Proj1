import sys
import cx_Oracle
import string
import getpass

def updatePatient(connection, curs):
    patient_id = input("\nEnter patient health care number: ")
    try:
        query = "SELECT * FROM patient WHERE health_care_no = " + patient_id
        curs.execute(query)
        result = curs.fetchall()
        print(result)
        #patient not in table yet
        if len(result) == 0:
            print("Patient doesn't exist - insert new patient.")
            #insertNewPatient(patient_id, connection, curs)
            name = input("Enter patient name: ")
            address = input("Enter patient's address: ")
            birth = input("Enter patient's birth date in YYYY-MM-DD format: ")
            phone = input("Enter patient's phone number: ")
            patient = (patient_id, name, address, birth, phone)
            print(patient)
            query = "INSERT INTO patient values ("+patient_id+", '"+name+"', '"+address+"', date '"+birth+"', '"+phone+"')"
            try:
                print(query)
                #this doesn't work - hangs
                curs.execute(query)
                connection.commit()
                print("Patient inserted.\n")
            except:
                print("Error doing stuff")
            return  
        else:
            #can update patient info - ask which info
            print("Update patient info - enter new info or press enter to skip.")
            name = input("Enter patient name: ")
            if name != "":
                try:
                    # works: needs '' around name
                    query = "UPDATE patient set name = '"+name+"' where health_care_no = "+patient_id
                    curs.execute(query)
                    connection.commit()
                except:
                    print("Error updating name")
            address = input("Enter patient's address: ")
            if address != '':
                try:
                    query = "UPDATE patient set address = '"+address+"' where health_care_no = "+patient_id
                    curs.execute(query)
                    connection.commit()
                except:
                    print("Error updating address")
            birth = input("Enter patient's birth date in YYYY-MM-DD format: ")
            if birth != '':
                try:
                    query = "UPDATE patient set birth_day = date '"+birth+"' where health_care_no = "+patient_id
                    curs.execute(query)
                    connection.commit()
                except:
                    print("Error updating birth date")
            phone = input("Enter patient's phone number: ")
            if phone != '':
                try:
                    query = "UPDATE patient set phone = '"+phone+"' where health_care_no = "+patient_id
                    curs.execute(query)
                    connection.commit()
                except:
                    print("Error updating phone")
        print("Patient info updated.\n")
        return
    except:
        print("Error finding patient health care number.")


def insertNewPatient(patient_id, connection, curs):
    name = input("Enter patient name: ")
    address = input("Enter patient's address: ")
    birth = input("Enter patient's birth date in YYYY-MM-DD format: ")
    phone = input("Enter patient's phone number: ")
    patient = (patient_id, name, address, birth, phone)
    print(patient)
    query = "INSERT INTO patient values ("+patient_id+", '"+name+"', '"+address+"', date '"+birth+"', '"+phone+"')"
    try:
        print(query)
        #this doesn't work - hangs
        curs.execute(query)
        connection.commit()
    except:
        print("Error doing stuff")
    return  
