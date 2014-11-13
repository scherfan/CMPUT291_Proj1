import cx_Oracle

def alarmingPatient(connection, curs):
    try:
        query = "DROP VIEW medical_risk"
        curs.execute(query)
        # create medical_risk view
        query2 = """
CREATE VIEW medical_risk(medical_type,alarming_age,abnormal_rate) AS
SELECT c1.type_id,min(c1.age),ab_rate
FROM  
      -- Find the abnormal rate for each test type
     (SELECT   t1.type_id, count(distinct t1.patient_no)/count(distinct t2.patient_no) ab_rate
      FROM     test_record t1, test_record t2
      WHERE    t1.result <> 'normal' AND t1.type_id = t2.type_id
      GROUP BY t1.type_id
      ) r,
	-- Find the abnormal result count above each age
     (SELECT   t1.type_id,age,COUNT(distinct p1.health_care_no) AS ab_cnt
      FROM     patient p1,test_record t1,
               (SELECT DISTINCT trunc(months_between(sysdate,p1.birth_day)/12) AS age FROM patient p1) 
      WHERE    trunc(months_between(sysdate,p1.birth_day)/12)>=age
               AND p1.health_care_no=t1.patient_no
               AND t1.result<>'normal'
      GROUP BY age,t1.type_id
      ) c1, 
 	 --- Find the patient count above each age
      (SELECT  t1.type_id,age,COUNT(distinct p1.health_care_no) AS cnt
       FROM    patient p1, test_record t1,
      	       (SELECT DISTINCT trunc(months_between(sysdate,p1.birth_day)/12) AS age FROM patient p1)
       WHERE trunc(months_between(sysdate,p1.birth_day)/12)>=age
             AND p1.health_care_no=t1.patient_no
       GROUP BY age,t1.type_id
      ) c2
WHERE  c1.age = c2.age AND c1.type_id = c2.type_id AND c1.type_id = r.type_id 
       AND c1.ab_cnt/c2.cnt>=2*r.ab_rate
GROUP BY c1.type_id,ab_rate"""

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
                    query3 = """SELECT DISTINCT health_care_no, name, address, phone
FROM   patient p, medical_risk m, test_type tt
WHERE  trunc(months_between(sysdate,birth_day)/12) >= m.alarming_age 
AND
       p.health_care_no NOT IN (SELECT patient_no
                                FROM   test_record t
                                WHERE  m.medical_type = t.type_id
                               )
AND tt.type_id = medical_type
AND tt.test_name = '"""+test+"'"
                    try:
                        curs.execute(query3)
                        result = curs.fetchall()
                        if len(result) == 0:
                            # either no patients have taken the test or no patients of alarming age
                            print("No patients of alarming age for this test.\n")
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
       
