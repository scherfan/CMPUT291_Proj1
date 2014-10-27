DELETE FROM test_record;
DELETE FROM not_allowed;
DELETE FROM can_conduct;
DELETE FROM test_type;
DELETE FROM medical_lab;
DELETE FROM doctor;
DELETE FROM patient;

INSERT INTO patient VALUES(
	1502, 'Bob Beck', '1025 Long Street Edmonton', to_date('07/15/1987', 'MM/DD/YYYY'),'5551239876'
);

INSERT INTO patient VALUES(
	1669, 'Richard Richards', '457 Lonely Man Avenue', to_date('02/23/1923', 'MM/DD/YYYY'), '5557829669'
);
	
INSERT INTO patient VALUES(
	1742, 'Mike Legend', '107 Avenue Edmonton', to_date('03/13/1957', 'MM/DD/YYYY'), '5554129875'
);

INSERT INTO patient VALUES(
	1478, 'Casper Freud', '785 Totally Quebec Street', to_date('11/29/1997', 'MM/DD/YYYY'), '5556521489'
);

INSERT INTO patient VALUES(
	1544, 'Mips Armtel', '452 Short Long Avenue Edmonton', to_date('10/07/1983', 'MM/DD/YYYY'), '5554782135'
);

INSERT INTO patient VALUES(
	2004, 'Steve Gates', '1998 Money Money Street', to_date('05/23/1972', 'MM/DD/YYYY'), '5559861222'
);

INSERT INTO patient VALUES(
	4220, 'Kim Kim', '124 Lost Street Edmonton', to_date('08/21/1980', 'MM/DD/YYYY'), '5557421554'
);

INSERT INTO patient VALUES(
	1504, 'Maybe Kinda', '699 Im Here I Think', to_date('03/15/1978', 'MM/DD/YYYY'), '5559633698'
);

INSERT INTO patient VALUES(
	4520, 'Garrus Vakarian', '455 Renegade Place', to_date('11/13/1984', 'MM/DD/YYYY'), '5554125454'
);

INSERT INTO patient VALUES(
	7878, 'Mister Man', '1546 Man Cave Cave', to_date('12/09/1845', 'MM/DD/YYYY'), '5551489875'
);

INSERT INTO doctor VALUES(
	130, '14 Hope Street', '4447986453', '9991234567', 1502
);

INSERT INTO doctor VALUES(
	187, '75 Doctor Lane', '4442345786', '9997452136', 1669
);

INSERT INTO doctor VALUES(
	154, '47 Missing Street', '4441597245', '9991592347', 1742
);

INSERT INTO doctor VALUES(
	487, '87 Edmonton Clinic', '4448775555', '9991123357', 1478
);

INSERT INTO doctor VALUES(
	231, '21 Quebec City Clinic', '4442245987', '9995879142', 1544
);

INSERT INTO doctor VALUES(
	111, '13 Victoria City Clinic', '4444554689', '9991254781', 2004
);

INSERT INTO doctor VALUES(
	121, '54 Toronto Clinic', '4448751254', '9996521962', 4220
);

INSERT INTO doctor VALUES(
	354, '93 Vancouver Clinic', '4447413695', '9994571236', 1504
);

INSERT INTO doctor VALUES(
	878, '41 Calgary Clinic', '4445567458', '9996541237', 4520
);

INSERT INTO doctor VALUES(
	598, '94 Vancouver Clinic', '4448739821', '9991249851', 7878
);

INSERT INTO medical_lab VALUES(
	'Lab One', '1 Medical Lane', '222157845'
);

INSERT INTO medical_lab VALUES(
	'Lab Two', '2 Medical Lane', '2227548978'
);

INSERT INTO medical_lab VALUES(
	'Lab Three', '3 Medical Lane', '2226981254'
);

INSERT INTO medical_lab VALUES(
	'Lab Four', '4 Medical Lane', '2229851478'
);

INSERT INTO medical_lab VALUES(
	'Lab Five', '5 Medical Lane', '2229651258'
);

INSERT INTO medical_lab VALUES(
	'Lab Six', '6 Medical Lane', '2229524871'
);

INSERT INTO medical_lab VALUES(
	'Lab Seven', '7 Medical Lane', '2227493224'
);

INSERT INTO medical_lab VALUES(
	'Lab Eight', '8 Medical Lane', '2223217854'
);

INSERT INTO medical_lab VALUES(
	'Lab Nine', '9 Medical Lane', '2226981268'
);

INSERT INTO medical_lab VALUES(
	'Lab Ten', '10 Medical Lane', '2229217888'
);

INSERT INTO test_type VALUES(
	15470, 'CT scan', 'Can do CT scan', 'Do a CT scan'
);

INSERT INTO test_type VALUES(
	18746, 'bone marrow check', 'Compatibility test', 'Take bone marrow from person'
);

INSERT INTO test_type VALUES(
	97878, 'X ray', 'N/A', 'Conduct X ray'
);

INSERT INTO test_type VALUES(
	54781, 'Taste test', 'Doctor recommednation', 'Patient must taste many types of food and determine their worth.'
);

INSERT INTO test_type VALUES(
	23547, 'IQ test', 'Patient must be willing to take the test', 'Patient is given questions and means to record answers'
);

INSERT INTO test_type VALUES(
	12547, 'Personality test', 'Doctor recommendation', 'Patient is asked to answer various questions about how they would react in a certain situation'
);

INSERT INTO test_type VALUES(
	95222, 'Color blind test', 'Patient must insist that they are color blind', 'Patient is given colors and asked say what color they see'
);

INSERT INTO test_type VALUES(
	78411, 'Physical check up', 'Patient health must be in question', 'Patient is given physically strenuous tasks and asked to do them for as long as possible'
);

INSERT INTO test_type VALUES(
	32687, 'Hearing test', 'Patient must have reported hearing loss', 'Various sounds are made and the patient is asked if they can hear each of the sounds'
);

INSERT INTO test_type VALUES(
	54231, 'Touch test', 'Patient must have reported loss of senses in their excremities', 'Patient is poked and touched by various objects to gauge reaction of the senses'
);

INSERT INTO can_conduct VALUES(
	'Lab One', 15470
);

INSERT INTO can_conduct VALUES(
	'Lab Two', 18746
);

INSERT INTO can_conduct VALUES(
	'Lab Three', 97878
);

INSERT INTO can_conduct VALUES(
	'Lab Four', 54781
);

INSERT INTO can_conduct VALUES(
	'Lab Five', 23547
);

INSERT INTO can_conduct VALUES(
	'Lab Six', 12547
);

INSERT INTO can_conduct VALUES(
	'Lab Seven', 95222
);

INSERT INTO can_conduct VALUES(
	'Lab Eight', 78411
);

INSERT INTO can_conduct VALUES(
	'Lab Nine', 32687
);

INSERT INTO can_conduct VALUES(
	'Lab Ten', 54231
);

INSERT INTO not_allowed VALUES(
	1502, 15470
);

INSERT INTO not_allowed VALUES(
	1669, 18746
);

INSERT INTO not_allowed VALUES(
	1742, 97878
);

INSERT INTO not_allowed VALUES(
	1478, 54781
);

INSERT INTO not_allowed VALUES(
	1544, 23547
);

INSERT INTO not_allowed VALUES(
	2004, 12547
);

INSERT INTO not_allowed VALUES(
	4220, 95222
);

INSERT INTO not_allowed VALUES(
	1504, 78411
);

INSERT INTO not_allowed VALUES(
	4520, 32687
);

INSERT INTO not_allowed VALUES(
	7878, 54231
);

INSERT INTO test_record VALUES(	
	1, 15470, 1544, 354, 'Lab One', 'normal', to_date('07/13/2011', 'MM/DD/YYYY'), to_date('07/16/2011', 'MM/DD/YYYY')
);

INSERT INTO test_record VALUES(	
	2, 18746, 4220, 598, 'Lab Two', 'normal', to_date('11/07/2014', 'MM/DD/YYYY'), to_date('12/01/2014', 'MM/DD/YYYY')
);

INSERT INTO test_record VALUES(	
	3, 97878, 1669, 130, 'Lab Three', 'abnormal', to_date('01/13/2013', 'MM/DD/YYYY'), to_date('01/14/2013', 'MM/DD/YYYY')
);

INSERT INTO test_record VALUES(	
	4, 54781, 1504, 878, 'Lab Four', 'normal', to_date('02/13/1997', 'MM/DD/YYYY'), to_date('02/19/1997', 'MM/DD/YYYY')
);

INSERT INTO test_record VALUES(	
	5, 23547, 1478, 187, 'Lab Five', 'abnormal', to_date('12/29/2013', 'MM/DD/YYYY'), to_date('01/13/2014', 'MM/DD/YYYY')
);

INSERT INTO test_record VALUES(	
	6, 15470, 1544, 354, 'Lab One', 'normal', to_date('07/13/2013', 'MM/DD/YYYY'), to_date('07/18/2013', 'MM/DD/YYYY')
);

INSERT INTO test_record VALUES(	
	7, 15470, 1544, 354, 'Lab One', 'normal', to_date('08/13/2013', 'MM/DD/YYYY'), to_date('08/18/2013', 'MM/DD/YYYY')
);

INSERT INTO test_record VALUES(	
	8, 15470, 1544, 354, 'Lab One', 'normal', to_date('09/13/2013', 'MM/DD/YYYY'), to_date('09/19/2013', 'MM/DD/YYYY')
);



/* Patients */
insert into patient values
(
	1234567890,
 	'John Farr',
 	'10256 NotSoCreative Ave Edmonton, Alberta T6Q-1m5', 
 	to_date('1985-02-09','YYYY-MM-DD'), 
 	'1888234678'
);
insert into patient values
(
	2892091320,
 	'Steve Smyth',
 	'5632 101 St Edmonton, Alberta T6Q-1M5', 
 	to_date('1970-12-17','YYYY-MM-DD'), 
 	'1426789234'
);
insert into patient values
(
	1123138491,
 	'Tim Bradly',
 	'8783 78 Ave Edmonton, Alberta T6Q-1Z6', 
 	to_date('1978-08-17','YYYY-MM-DD'), 
 	'7803456666'
);
insert into patient values
(
	1398232948,
 	'Dave Smyth',
 	'5632 101 St Edmonton, Alberta T6Q-1M5', 
 	to_date('1963-12-17','YYYY-MM-DD'), 
 	'4881291234'
);
insert into patient values
(
	3898414320,
 	'Cody Dale',
 	'6782 155 St Edmonton, Alberta T6Q-1M5', 
 	to_date('1975-05-20','YYYY-MM-DD'), 
 	'7803442199'
);
insert into patient values
(
	4000987892,
 	'Ryan Carsen',
 	'13421 44 Ave Stony Plain, Alberta T5L-1B3', 
 	to_date('1966-11-12','YYYY-MM-DD'), 
 	'5768927483'
);
insert into patient values
(
	8789909099,
 	'Jim Lowe',
 	'56334 Barlow St Pidgeon Lake, Alberta T5R-1L5', 
 	to_date('1988-01-01','YYYY-MM-DD'), 
 	'5762830198'
);
insert into patient values
(
	5009988972,
 	'Carl Lazenby',
 	'3439 Beach Lane Silvan Lake, Alberta T2P-1E1', 
 	to_date('1963-12-17','YYYY-MM-DD'), 
 	'7809991233'
);
insert into patient values
(
	8874238722,
 	'Rodger Royale',
 	'2432 King St Spruce Grove, Alberta T5R-2M3', 
 	to_date('1944-05-22','YYYY-MM-DD'), 
 	'7809637777'
);
insert into patient values
(
	2378371819,
 	'Bob Tall',
 	'13781 105 St Edmonton, Alberta T6Q-9B4', 
 	to_date('1967-10-09','YYYY-MM-DD'), 
 	'7802340123'
);

/* Doctors */
insert into doctor values
(
	1234542342,
	'3241 265 St Edmonton, AB TR5-1B6',
	'1888456983',
	'1099283572',
	1123138491	
);
insert into doctor values
(
	3948320982,
	'4453 119 St Edmonton, AB TR5-1B6',
	'1755194829',
	'1099200764',
	1234567890
);
insert into doctor values
(
	9887176236,
	'15534 200 Ave Edmonton, AB TR5-7Y7',
	'7809845264',
	'7806354727',
	1398232948
);

/* Medical Labs */
insert into medical_lab values
(
	'This is Not A Lab',
	'2341 104 Ave Edmonton, Alberta Y8t-1d3',
	'1283028472'
);
insert into medical_lab values
(
	'The Oh-So-Helpful Lab',
	'2341 105 Ave Edmonton, Alberta Y8t-1d3',
	'1893920483'
);
insert into medical_lab values
(
	'Johnsons Medical Lab',
	'10321 106 St Edmonton, Alberta Y8t-1P2',
	'7809848183'
);

/* test types */
insert into test_type values
(
	12314,
	'Funny Bone Itch Test',
	'Patient must have a funny bone and a sense of humour.',
	'Proceed to tickle funny bone with feather.'
);
insert into test_type values
(
	56789,
	'Turing Test',
	'Patient must be arguably an artificial intelligence or human. Another participant is required.',
	'Proceed to administer Turing test.'
);
insert into test_type values
(
	44633,
	'CT scan',
	'Patient able to be moved and having no metal in or on body.',
	'Set patient in scanning machine, remove metal items, scan.'
);
insert into test_type values
(
	27398,
	'bone marrow check',
	'Patient must have bones and vertebrae.',
	'Take a spinal tap for bone marrow.'
);
insert into test_type values
(
	87839,
	'X ray',
	'Patient must not have had less than 5 x-rays in the last 24-hrs.',
	'Place lead vest on sensitive areas, position x-rayed area, scan.'
);

/* Labs that can Consuct tests */
insert into can_conduct values
(
	'This is Not A Lab', 
	87839
);
insert into can_conduct values
(
	'This is Not A Lab', 
	27398
);
insert into can_conduct values
(
	'This is Not A Lab', 
	44633
);
insert into can_conduct values
(
	'This is Not A Lab', 
	56789
);
insert into can_conduct values
(
	'This is Not A Lab', 
	12314
);
insert into can_conduct values
(
	'The Oh-So-Helpful Lab', 
	12314
);
insert into can_conduct values
(
	'The Oh-So-Helpful Lab', 
	56789
);
insert into can_conduct values
(
	'Johnsons Medical Lab',
	44633
);
insert into can_conduct values
(
	'Johnsons Medical Lab', 
	27398
);
insert into can_conduct values
(
	'Johnsons Medical Lab', 
	87839
);

/* Patients and the test's they are not allowed to take */
insert into not_allowed values
(
	1123138491,
	12314
);
insert into not_allowed values
(
	1123138491,
	56789
);
insert into not_allowed values
(
	1123138491,
	44633
);
insert into not_allowed values
(
	1123138491,
	27398
);
insert into not_allowed values
(
	1123138491,
	87839
);
insert into not_allowed values
(
	2892091320,
	27398
);
insert into not_allowed values
(
	2892091320,
	12314
);
insert into not_allowed values
(
	3898414320,
	44633
);
insert into not_allowed values
(
	3898414320,
	27398
);
insert into not_allowed values
(
	3898414320,
	87839
);
insert into not_allowed values
(
	3898414320,
	12314
);
insert into not_allowed values
(
	4000987892,
	87839
);
insert into not_allowed values
(
	8789909099,
	27398
);
insert into not_allowed values
(
	8874238722,
	44633
);

/* patient's test records */
insert into test_record values
(
	1000000190,
	56789,
	3898414320,
	1234542342,
	'This is Not A Lab',
	'normal',
	to_date('2010-01-01','YYYY-MM-DD'),
	to_date('2010-05-10','YYYY-MM-DD')
);
insert into test_record values
(
	1000000191,
	56789,
	3898414320,
	1234542342,
	'This is Not A Lab',
	'normal',
	to_date('2011-01-01','YYYY-MM-DD'),
	to_date('2011-10-05','YYYY-MM-DD')
);
insert into test_record values
(
	1000000192,
	56789,
	3898414320,
	1234542342,
	'This is Not A Lab',
	'abnormal',
	to_date('2012-03-03','YYYY-MM-DD'),
	to_date('2012-09-13','YYYY-MM-DD')
);
insert into test_record values
(
	1000000295,
	44633,
	4000987892,
	9887176236,
	'Johnsons Medical Lab',
	'abnormal',
	to_date('2013-02-03','YYYY-MM-DD'),
	to_date('2013-03-12','YYYY-MM-DD')
);
insert into test_record values
(
	1000000296,
	44633,
	4000987892,
	9887176236,
	'Johnsons Medical Lab',
	'abnormal',
	to_date('2013-04-14','YYYY-MM-DD'),
	to_date('2013-10-15','YYYY-MM-DD')
);
insert into test_record values
(
	1000000297,
	44633,
	4000987892,
	9887176236,
	'Johnsons Medical Lab',
	'normal',
	to_date('2013-04-15','YYYY-MM-DD'),
	to_date('2013-11-16','YYYY-MM-DD')
);
insert into test_record values
(
	1000000380,
	87839,
	2892091320,
	3948320982,
	'Johnsons Medical Lab',
	'abnormal',
	to_date('2011-11-24','YYYY-MM-DD'),
	to_date('2011-12-16','YYYY-MM-DD')
);
insert into test_record values
(
	1000000381,
	87839,
	2892091320,
	3948320982,
	'Johnsons Medical Lab',
	'normal',
	to_date('2012-11-24','YYYY-MM-DD'),
	to_date('2012-12-16','YYYY-MM-DD')
);
insert into test_record values
(
	1000000450,
	27398,
	8874238722,
	1234542342,
	'Johnsons Medical Lab',
	'abnormal',
	to_date('2010-11-22','YYYY-MM-DD'),
	to_date('2010-12-01','YYYY-MM-DD')
);
insert into test_record values
(
	1000000451,
	27398,
	8874238722,
	1234542342,
	'Johnsons Medical Lab',
	'abnormal',
	to_date('2011-11-22','YYYY-MM-DD'),
	to_date('2011-12-01','YYYY-MM-DD')
);
insert into test_record values
(
	1000000460,
	12314,
	8789909099,
	1234542342,
	'The Oh-So-Helpful Lab',
	'normal',
	to_date('2013-12-24','YYYY-MM-DD'),
	to_date('2013-12-24','YYYY-MM-DD')
);
insert into test_record values
(
	1000000461,
	44633,
	8789909099,
	1234542342,
	'Johnsons Medical Lab',
	'normal',
	to_date('2013-12-20','YYYY-MM-DD'),
	to_date('2013-12-30','YYYY-MM-DD')
);



