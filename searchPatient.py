# Search for a patient test records

from prescribeTest import *

def searchPatient(connection, curs):
	error = True
	while error:
		patient = input("\nPatient Name (enter 1) or Patient Health Care # (enter 2): ")
		if int(patient) == 1:
			patient = input("  Patient Name: ")
			error = False
		elif int(patient) == 2:
			patient = input("  Patient Health Care #: ")
			patient = int(patient)
			error = False

	findTestRecords(patient, curs)

def findTestRecords(patient, curs):
	if type(patient) == str:
		patient_id = getPatientId(patient, curs)
		patient_name = patient
		if patient_id == 1:
			return
		#print(patient_id)
	else:
		patient_id = patient
		patient_name = getPatientName(patient_id, curs)
		if patient_name == 1:
			return
		#print(patient_id, patient_name)


	try:
		query = "SELECT DISTINCT p.name, p.health_care_no, t.test_name, r.test_date, r.result "
		query += "FROM patient p, test_type t, test_record r "
		query += "WHERE p.health_care_no = " + str(patient_id) + " "
		query += "AND p.name LIKE '"+patient_name+"' "
		query += "AND t.type_id = r.type_id "
		query += "AND r.patient_no = p.health_care_no" 
		#print(query)
		curs.execute(query)
		results = curs.fetchall()
		if len(results) == 0:
			print("  No test records available")
		else:
			rnd = 1
			for result in results:
				row = [result[0], result[1], result[2], result[3], result[4]]
				for i in range(0, len(row)):
					if row[i] == None:
						row[i] = "N/A"

				print("\nTest " + str(rnd))
				output = "Patient Name: " + row[0]
				output += "\nHealth Care Number: " + str(row[1])
				output += "\nTest taken: " + row[2]
				output += "\nDate taken: " + str(row[3])
				output += "\nResult: " + row[4]
				print(output)
				rnd += 1
				#print(result)
		print('')

	except:
		print('Error at findTestRecords')


def getPatientName(id, curs):
	try:
		query = "SELECT name "
		query += "FROM patient "
		query += "WHERE health_care_no = " + str(id)
		curs.execute(query)
		result = curs.fetchall()
		if len(result) == 0:
			print("  No patient found\n")
			return 1
		return result[0][0]

	except:
		print('Error at getPatientname')
		return 1


		
