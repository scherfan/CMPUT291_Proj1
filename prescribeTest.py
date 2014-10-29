# Prescription file

def prescribeTest():
	#print("Imported")
	doctor = input("\nDoctor Name (enter 1) or Doctor Id (enter 2): ")
	if int(doctor) == 1:
		doctor_name = input("  Name of the Doctor: ")
	elif int(doctor) == 2:
		doctor_id = input("  Id of the Doctor: ")

	testname = input("\nEnter the name of the test: ")

	patient = input("\nPatient Name (enter 1) or Patient Id (enter 2): ")
	if int(patient) == 1:
		patient_name = input("  Name of the Patient: ")
	elif int(patient) == 2:
		patient_id = input("  Id of the Patient: ")

	return
