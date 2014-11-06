# Search for a patient test records
""" List the health_care_no, patient name, 
    test type name, testing date, and test 
    result of all test records """
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
		#print(patient_id)
	else:
		patient_id = patient
		patient_name = getPatientName(patient_id, curs)
		#print(patient_id, patient_name)


	try:
		query = "SELECT DISTINCT p.name, p.health_care_no, t.test_name, r.test_date, r.result "
		query += "FROM patient p, test_type t, test_record r "
		query += "WHERE p.health_care_no = " + str(patient_id) + " "
		query += "AND p.name LIKE '"+patient_name+"' "
		query += "AND r.patient_no = " + str(patient_id)
		#print(query)
		curs.execute(query)
		results = curs.fetchall()
		for result in results:
			print(result)
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
		return result[0][0]

	except:
		print('Error at getPatientname')
		return 1


		
