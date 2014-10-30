# Prescription file

def prescribeTest(connection, curs):
	error = True

	while error == True:
		doctor = input("\nDoctor Name (enter 1) or Doctor Id (enter 2): ")
		if int(doctor) == 1:
			doctor_name = input("  Name of the Doctor: ")
			error = checkForDoctorName(doctor_name, curs);
			if error == True:
				continue
			#else:
				#print("  Found doctor: " + doctor_name)
		elif int(doctor) == 2:
			doctor_id = input("  Id of the Doctor: ")
			error = checkForDoctorId(doctor_id, curs)
			if error == True:
				continue

		testname = input("\nEnter the name of the test: ")
		error = findTest(testname, curs)

		#patient = input("\nPatient Name (enter 1) or Patient Id (enter 2): ")
		#if int(patient) == 1:
			#patient_name = input("  Name of the Patient: ")
		#elif int(patient) == 2:
			#patient_id = input("  Id of the Patient: ")



	return


def checkForDoctorName(name, curs):
	try:
		query = "SELECT p.name "  
		query += "FROM patient p, doctor d "
		query += "WHERE p.name LIKE '"+name+"' "
		query += "AND p.health_care_no = d.health_care_no"
		#print(query)
		curs.execute(query)
		result = curs.fetchall()
		#print(result)
		if len(result) == 0:
			print("  Doctor not found in database, please try again")
			return True
		else:
			return False
		#print(result)

	except:
		print("Error")
		return True

def checkForDoctorId(id, curs):
	try:
		query = "SELECT employee_no "
		query += "FROM doctor "
		query += "WHERE employee_no = " + id
		#print(query)
		curs.execute(query)
		result = curs.fetchall()
		if len(result) == 0:
			print("  Doctor not found in database, please try again")
			return True
		else:
			return False

	except:
		print("Error")
		return True

def findTest(testname, curs):
	try:
		query = "SELECT test_name "
		query += "FROM test_type "
		query += "WHERE test_name LIKE '"+testname+"'"
		curs.execute(query)
		result = curs.fetchall()
		if len(result) == 0:
			print("  Test not found, please try again")
			return True
		else:
			return False

	except:
		print("Error at findTest")
		return True