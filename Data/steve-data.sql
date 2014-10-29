/*
 * Steven Cherfan
 * CMPUT 291
 * Populates database for Asn 2.
 */

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