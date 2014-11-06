# Patient information update

def searchPatient(connection, curs):
	patient = input("\nPatient name (enter 1) or Patient health care number (enter 2): ")
	if int(patient) == 1:
		patient_name = input(" Name of patient: ")
		
