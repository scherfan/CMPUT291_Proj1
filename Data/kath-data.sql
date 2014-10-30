insert into patient values(1000, 'Sherlock Holmes', '221b Baker St London', date '1975-01-01', '7801234567');
insert into patient values(1001, 'John Watson', '155 St Vancouver', date '1980-05-19', '7800000000');
insert into patient values(1002, 'Richard Richards', '10001 Ontario', date '1942-03-18', '7800987654');
insert into patient values(1003, 'Dr House', '100 St Edmonton', date '1964-06-11', '7804355555');
insert into patient values(1004, 'Dr Wilson', '200 St Edmonton', date '1988-05-04', '7804251234');
insert into patient values(1005, 'James Kirk', '911 Edmonton', date '1988-07-14', '7809696969');
insert into patient values(1006, 'Spock', '11111 11 Ave Edmonton', date '1942-02-14', '7801112222');

insert into medical_lab values('Lab 1', '10101 Edmonton', '7801010101');
insert into medical_lab values('Lab 2', '99999 Edmonton', '7809999999');
insert into medical_lab values('Lab 3', '111 11 Edmonton', '7808675234');

insert into medical_lab values('Lab 4', '1234 Edmonton', '7802223333');

insert into doctor values(2000, '19191 Edmonton', '7809098000', '7804355555', 1003);
insert into doctor values(2001, '10000 Edmonton', '7808008000', '7804251234', 1004);


insert into test_type values(1, 'CT Scan', 'have problem', 'do a scan');
insert into test_type values(2, 'bone marrow check', 'bone problem', 'check bone marrow');
insert into test_type values(3, 'X ray', 'something broken', 'do an x-ray');

insert into can_conduct values('Lab 1', 1);
insert into can_conduct values('Lab 2', 2);
insert into can_conduct values('Lab 1', 3);
insert into can_conduct values('Lab 3', 2);
insert into can_conduct values('Lab 3', 3);
insert into can_conduct values('Lab 1', 2);
insert into can_conduct values('Lab 2', 1);
insert into can_conduct values('Lab 4', 1);

insert into not_allowed values(1000, 1);
insert into not_allowed values(1001, 3);
insert into not_allowed values(1004, 2);

insert into test_record values(1, 1, 1002, 2000, 'Lab 1', 'abnormal', date '2014-09-14', date '2014-10-04');
insert into test_record values(2, 1, 1003, 2000, 'Lab 2', 'abnormal', date '2013-01-01', date '2013-01-11');
insert into test_record values(3, 1, 1004, 2001, 'Lab 1', 'normal', date '2013-09-14', date '2013-10-04');
insert into test_record values(4, 2, 1004, 2001, 'Lab 2', 'normal', date '2013-08-14', date '2014-09-04');
insert into test_record values(5, 1, 1004, 2001, 'Lab 1', 'normal', date '2013-06-10', date '2013-07-01');
insert into test_record values(6, 1, 1004, 2001, 'Lab 1', 'normal', date '2013-12-01', date '2014-01-03');
insert into test_record values(7, 2, 1002, 2000, 'Lab 2', 'normal', date '2013-11-14', date '2013-11-20');
insert into test_record values(8, 2, 1002, 2001, 'Lab 2', 'normal', date '2014-03-13', date '2014-04-13');

insert into test_record values(9, 2, 1000, 2001, 'Lab 3', 'normal', date '2014-04-09', date '2014-04-15');
insert into test_record values(10, 1, 1003, 2000, 'Lab 1', 'normal', date '2011-01-01', date '2011-01-11');
insert into test_record values(11, 2, 1000, 2000, 'Lab 3', 'abnormal', date '2012-02-21', date '2012-03-02');
insert into test_record values(12, 2, 1000, 2000, 'Lab 3', 'normal', date '2012-03-20', date '2012-03-25');

insert into test_record values(13, 2, 1001, 2001, 'Lab 2', 'abnormal', date '2014-03-20', date '2014-04-04');
insert into test_record values(14, 1, 1005, 2001, 'Lab 2', 'abnormal', date '2014-05-20', date '2014-06-04');
insert into test_record values(15, 2, 1005, 2000, 'Lab 1', 'abnormal', date '2013-01-20', date '2013-01-21');
insert into test_record values(16, 2, 1006, 2000, 'Lab 1', 'abnormal', date '2012-08-21', date '2012-08-22');
insert into test_record values(17, 3, 1006, 2001, 'Lab 1', 'abnormal', date '2010-11-11', date '2010-12-02');

insert into test_record values(18, 3, 1004, 2001, 'Lab 3', 'abnormal', date '2011-11-11', date '2011-11-12');
insert into test_record values(19, 3, 1004, 2001, 'Lab 1', 'normal', date '2012-09-12', date '2012-09-22');
insert into test_record values(20, 3, 1005, 2000, 'Lab 1', 'normal', date '2010-10-05', date '2010-10-08');

insert into test_record values(21, 1, 1005, 2000, 'Lab 4', 'normal', date '2014-07-02', date '2014-07-08');









