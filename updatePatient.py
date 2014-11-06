import sys
import cx_Oracle
import string
import getpass
import datetime

def updatePatient(connection, curs):
    patient_id = input("\nEnter patient health care number: ")
    try:
        query = "SELECT * FROM patient WHERE health_care_no = " + patient_id
        curs.execute(query)
        result = curs.fetchall()
        #patient not in table yet
        if len(result) == 0:
            print("Patient doesn't exist - insert new patient.\n")
            name = input("Enter patient name: ")
            address = input("Enter patient's address: ")
            birth = input("Enter patient's birth date in YYYY-MM-DD format: ")
            phone = input("Enter patient's phone number: ")
            patient = (patient_id, name, address, birth, phone)
            print(patient)
            query = "INSERT INTO patient values ("+patient_id+", '"+name+"', '"+address+"', date '"+birth+"', '"+phone+"')"
            try:
                #print(query)
                #this doesn't work - hangs
                curs.execute(query)
                connection.commit()
                print("Patient added.\n")
            except:
                print("Error doing stuff")
            return  
        else:
            #can update patient info - ask which info
            print("\nPatient selected:")
            print("Health care number: "+str(result[0][0]))
            print("Name: "+result[0][1])
            print("Address: "+result[0][2])
            print("Birth date: "+str(result[0][3])[:10])
            print("Phone number: "+result[0][4]+"\n")
            print("Update patient info - enter new info or press enter to skip.")
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
    except:
        print("\nError finding patient health care number - must be an integer.\n")

