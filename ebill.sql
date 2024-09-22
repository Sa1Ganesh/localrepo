-- TO GENERATE ELECTRICITY BILL USING SQL
create table ebill(rrno varchar2(10),cus_name varchar2(50),bill_date date ,units number); 
desc ebill;
insert into ebill values('eh511','sai','15-aug-19',75);
insert into ebill values('eh512','akhil','16-aug-19',115);
insert into ebill values('eh513','ganesh','17-aug-19',95);
insert into ebill values('eh514','lokesh','18-aug-19',102);
insert into ebill values('eh515','rahul','19-aug-19',125);
insert into ebill values('eh516','dinesh','20-aug-19',97);
insert into ebill values('eh517','dadu','21-aug-19',99);
insert into ebill values('eh518','sathya','22-aug-19',138);

select * from ebill;
--drop table ebill;

alter table ebill add (bill_amt number(6,2),due_date date);
desc ebill;

update ebill set bill_amt =50;

update ebill set bill_amt =bill_amt+100*4.50+(units-100)*5.50 where units>100;
update ebill set bill_amt=bill_amt+100*4.50 where units<=100;

select * from ebill;

update ebill set due_date=bill_date+15;

select * from ebill;
