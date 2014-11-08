import cx_Oracle

def alarmingPatient(connection, curs):
    try:
        query = "DROP VIEW medical_risk"
        curs.execute(query)
        # create medical_risk view
        query2 = """
CREATE VIEW medical_risk
(medical_type, abnormal_rate, alarming_age) 
AS
SELECT tr3.type_id, COUNT(distinct tr1.test_id)/ COUNT(distinct tr2.test_id), Extract(YEAR from sysdate) - Extract(YEAR from p1.birth_day)
FROM test_record tr1, test_record tr2, test_record tr3, test_record tr4, patient p1, patient p2
WHERE tr1.type_id = tr2.type_id AND
	tr2.type_id = tr3.type_id AND
	tr3.type_id = tr4.type_id AND
	tr3.patient_no = p1.health_care_no AND
	tr4.patient_no = p2.health_care_no AND
	Extract(YEAR from p1.birth_day) = Extract(YEAR from p2.birth_day) AND
	tr1.result <> 'normal' AND
	tr3.result <> 'normal'
GROUP BY tr3.type_id, (Extract(YEAR from sysdate) - Extract(YEAR from p1.birth_day))
HAVING (COUNT(distinct tr3.test_id) / COUNT(distinct tr4.test_id)) >= ALL(SELECT 2*(COUNT(distinct tr5.test_id) / COUNT(distinct tr6.test_id))
										FROM test_record tr5, test_record tr6
										WHERE tr5.type_id = tr6.type_id AND
											tr5.result <> 'normal' AND
											tr5.type_id = tr3.type_id
										GROUP BY tr5.type_id
										)"""
        curs.execute(query2)
        while (True):
            test = input("Input name of test: ")
            # make sure test exists
            query = "SELECT type_id FROM test_type WHERE test_name = '"+test+"'"
            try:
                curs.execute(query)
                test_id = curs.fetchall()
                if len(test_id) == 0:
                    # test doesn't exist - ask again
                    print("Test doesn't exist.")
                else:
                    # test does exist - get patient info from view
                    query3 = """SELECT health_care_no, name, address, phone
FROM (SELECT p.health_care_no, p.name, p.address, p.phone, m.medical_type
	FROM patient p, medical_risk m
	WHERE p.birth_day <= (sysdate - ((m.alarming_age-1)*365))
	MINUS
	SELECT distinct p1.health_care_no, p1.name, p1.address, p1.phone, m1.medical_type
	FROM patient p1, test_record tr2, medical_risk m1
	WHERE tr2.type_id = m1.medical_type AND
		tr2.patient_no = p1.health_care_no
	)
WHERE medical_type IN (SELECT type_id
                       FROM test_type
                       WHERE test_name = '"""+test+"')"
                    try:
                        curs.execute(query3)
                        result = curs.fetchall()
                        if len(result) == 0:
                            # either no patients have taken the test or no patients of alarming age
                            print("No patients of alarming age for this test.")
                        i = 0
                        #print results
                        while (i < len(result)):
                            print("\nHealth care number: "+str(result[i][0]))
                            print("Name: "+result[i][1])
                            print("Address: "+result[i][2])
                            print("Phone number: "+result[i][3]+"\n")
                            i += 1
                        break
                    except cx_Oracle.DatabaseError as ex:
                        error, = ex.args
                        print("Error code ="+str(error.code))
                        print("Error message ="+str(error.message))
            except cx_Oracle.DatabaseError as ex:
                error, = ex.args
                print("Error message ="+str(error.message))

    except cx_Oracle.DatabaseError as ex:
            error, = ex.args
            print("Error code ="+str(error.code))
            print("Error message ="+str(error.message))
            print("Error finding test")

    return
       
