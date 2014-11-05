def updatePatient(connection, curs):
    patient_id = input("\nEnter patient health care number: ")
    try:
        query = "SELECT * FROM patient WHERE health_care_no = " + patient_id
        curs.execute(query)
        result = curs.fetchall()
        #patient not in table yet
        if len(result) == 0:
            print("Patient doesn't exist - insert new patient.")
            name = input("Enter patient name: ")
            address = input("Enter patient's address: ")
            birth = input("Enter patient's birth date in YYYY-MM-DD format: ")
            phone = input("Enter patient's phone number: ")
            #need to insert into table
          #  query = "INSERT INTO patient "
            #pretty sure these have to be in [(1000, "name", "address", date, "phone")] format
           # query += "VALUES ("+patient_id+", "+name+", "+address+", "+birth+", "+phone+")"
            patient1 = (int(patient_id))
            patient2 = (name, address, birth, phone)
            patient = patient1+patient2
            curs.execute("INSERT INTO patient(health_care_no, name, address, birth_day, phone) "
                         "VALUES (:1, :2, :3, :4, :5)", patient)
            curs.commit()
            
            
            
        
