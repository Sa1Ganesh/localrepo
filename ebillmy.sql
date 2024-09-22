CREATE DATABASE BILL;
USE BILL;
-- TO GENERATE ELECTRICITY BILL USING SQL
create table ebill(rrno varchar(10),cus_name varchar(50),bill_date date ,units int); 
desc ebill;
insert into ebill values("eh511","sai","15-09-19",75);
insert into ebill values('eh512','akhil','15-09-21',115);
insert into ebill values('eh513','ganesh','15-09-23',95);
insert into ebill values('eh514','lokesh','15-09-25',102);
insert into ebill values('eh515','rahul','15-09-27',125);
insert into ebill values('eh516','dinesh','15-09-29',97);
insert into ebill values('eh517','dadu','15-09-29',99);
insert into ebill values('eh518','sathya','15-09-29',138);

select * from ebill;



alter table ebill add column bill_amt int;
alter table ebill add column due_date date;

desc ebill;

update ebill set bill_amt =50;
set sql_safe_updates =0;

update ebill set bill_amt =bill_amt+100*4.50+(units-100)*5.50 where units>100;
update ebill set bill_amt=bill_amt+100*4.50 where units<=100;

select * from ebill;

update ebill set due_date=(bill_date+interval 15 day);

select * from ebill;
