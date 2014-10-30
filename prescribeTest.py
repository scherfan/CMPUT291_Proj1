# Prescription file

def prescribeTest(connection, curs):
	
	# Finding Doctor in doctor values
	error = True
	while error == True:
		doctor = input("\nDoctor Name (enter 1) or Doctor Id (enter 2): ")
		if int(doctor) == 1:
			doctor_name = input("  Name of the Doctor: ")
			error = checkForDoctorName(doctor_name, curs)
			doctor = doctor_name
		elif int(doctor) == 2:
			doctor_id = input("  Employee Id of the Doctor: ")
			error = checkForDoctorId(doctor_id, curs)
			doctor = int(doctor_id)

	# Finding the test type in test values
	error = True
	while error == True:
		testname = input("\nEnter the name of the test: ")
		error = findTest(testname, curs)

	# Finding the Patient in patient values
	error = True
	while error == True:
		patient = input("\nPatient Name (enter 1) or Patient Id (enter 2): ")
		if int(patient) == 1:
			patient_name = input("  Name of the Patient: ")
			error = findPatientName(patient_name, curs)
			if error == False:
				patient = patient_name
		elif int(patient) == 2:
			patient_id = input("  Health Care # of the Patient: ")
			error = findPatientId(patient_id, curs)
			if error == False:
				patient = int(patient_id)

	# Check if patient can take the test
	error = True
	while error == True:
		error = checkAllowed(patient, testname, curs)




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
		print("Error at checkForDoctorName")
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
		print("Error at checkForDoctorId")
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


def findPatientName(patient_name, curs):
	try:
		query = "SELECT name "
		query += "FROM patient "
		query += "WHERE name LIKE '"+patient_name+"' "
		curs.execute(query)
		result = curs.fetchall()
		if len(result) == 0:
			print("  Patient not found, please try again")
			return True
		else:
			return False

	except:
		print("Error at findPatientName")
		return True


def findPatientId(patient_id, curs):
	try:
		query = "SELECT health_care_no "
		query += "FROM patient "
		query += "WHERE health_care_no = " + patient_id
		#print(query)
		curs.execute(query)
		result = curs.fetchall()
		if len(result) == 0:
			print("  Patient not found in database, please try again")
			return True
		else:
			return False

	except:
		print("Error at findPatientId")
		return True


def checkAllowed(patient, testname, curs):
	#print(patient, testname)
	if type(patient) == str:
		print("Patient is a string")
	elif type(patient) == int:
		#print("Patient is an integer")
		try:
			query = "SELECT DISTINCT p.health_care_no "
			query += "FROM not_allowed n, patient p, test_type t "
			query += "WHERE t.test_name LIKE '"+testname+"' "
			query += "AND p.health_care_no <> n.health_care_no "
			query += "AND t.type_id = n.test_id "
			query += "AND p.health_care_no = " + str(patient)
			curs.execute(query)
			result = curs.fetchall()

			if len(result) == 0:
				print("  Patient cannot take this test!")
			elif len(result) == 1:
				if result[0][0] == patient:
					print("  This patient can take the test")
			#print(result)
			return False

		except:
			print("Error at checkAllowed")
			return True
