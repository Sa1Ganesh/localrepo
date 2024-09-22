--TO CREATE STUDENT DATABASE AND TO CHECK THE RESULTS
--USING SQLDEVELOPER
create table student(s_id number,s_name varchar2(30),tel number,hin number ,eng number ,mat number,phy number,che number);
desc student;
insert into student values(1,'sai',95,90,93,96,97,95);
insert into student values(2,'zahan',33,90,83,96,87,94);
insert into student values(3,'umar',85,90,73,96,87,95);
insert into student values(4,'sathya',90,95,83,97,96,96);
insert into student values(5,'rajesh',97,80,93,96,97,94);
insert into student values(6,'lucky',88,92,83,96,97,95);
insert into student values(7,'viart',23,95,93,96,98,98);
insert into student values(8,'sam',95,80,97,96,99,94);
select * from student;
alter table student add (total number,per number,result varchar2(30));
update student set total=tel+hin+eng+mat+phy+che;
update student set per =total/6;
update student set result='pass' where tel>=35 and hin>=35 and eng>=35 and mat>=35 and phy>=35 and che>=35;
update student set result ='fail' where tel<35 or hin<35 or eng<35 or mat<35 or phy<35 or che<35;
select * from student;
select s_id,s_name from student;
select * from student where result='pass';
select * from student where result='fail';
select count(*) from student where result='pass';
select count(*) from student where result='fail';
select count(*) from student where per>90;
select * from student order by s_name;