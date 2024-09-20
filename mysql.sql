/*create database tem1;
CREATE DATABASE  tem2 ;
drop database tem1;
drop database tem2;*/
CREATE DATABASE college;
/*
CREATE DATABASE IF NOT EXISTS college;
DROP DATABASE IF EXISTS college;
SHOW DATABASES;
SHOW TABLES;
*/
USE college;
/*CREATE TABLE table_name(
column_name1 datatype constraint
column_name2 datatype constraint);*/
/*CREATE TABLE  student(
ID int primary key,
NAME varchar(50),
AGE int not null
);
INSERT INTO student VALUES (1,"sai",22);
INSERT INTO student VALUES(2,"sathya",14);
INSERT INTO student VALUES(3,"akhil",13);
SELECT * FROM student;
DROP TABLE student;*/
/*
DATATYPES
CHAR
VARCHAR
BLOB
INT
TINYINT SIGNED(-128 TO 127) / UNSIGNED(0 TO 255)
BIGINT
BIT
FLOAT
DOUBLE
BINARY
DATE
YEAR
BOOLEAN
*/
/* 
types of sql commands
DDL(DATA DEFINITION LANGUAGE): CREATE ,ALTER,RENAME,TRUNCATE,DROP
DQL(DATA QUERY LANGUAGE): SELECT
DML(DATA MANIPULATION LANGUAGE):INSERT,UPDATE,DELETE
DCL(DATA CONTROL LANGUAGE): GRANT and REVOKE (permission to users)
TCL(TRANSACTION CONTROL LANGUAGE): START TRANSACTION,COMMIT,ROLLBACK
*/
/* 
SELECT * FROM table_name #to view all columns
INSERT INTO table_name  VALUES(col1_v1,col2_v1),(col1_v2,col2_v2);
*/
/*
#p1
CREATE DATABASE svpc;
USE svpc;
CREATE TABLE Employee (
ID int primary key,
NAME  varchar(50),
SALARY int
);
INSERT INTO employee VALUES(1,"adam",25000),(2,"bob",30000),(3,"casey",40000);
SELECT * FROM employee;
DROP TABLE employee;
DROP DATABASE svpc;
*/
/*
Constraints
#to specify rules for data in a table

Not Null
#columns cannot have a null value

Unique
#all values in column are different

Primary key 
column (set of columns) to identify a row uniquely 
only 1 pk ,not null

ID int primary key
or 
CREATE TABLE examp(
ID int not null,
primary key(ID)
);

Foreign key
column (set of columns) to refer pk in another table
can be multiple fks
can have duplicate and null values

CREATE TABLE dept(
id INT PRIMARY KEY ,
name  VARCHAR(50)
);
 CREATE TABLE teacher (
 id INT PRIMARY KEY,
 name VARCHAR(50),
 dept_id INT,
 FOREIGN KEY (dept_id) REFERENCES dept(id)
 );
 

CREATE TABLE examp(
cust_id int,
foreign key (cust_id) references customer(id)
);

DEFAULT 
salary int DEFAULT 25000

Check
#it can limit values allowed in a column

CREATE TABLE license(
age INT CHECK (age>=18)
);
*/
/*
Constraints
#to specify rules for data in a table

Not Null
#columns cannot have a null value

Unique
#all values in column are different

Primary key 
column (set of columns) to identify a row uniquely 
only 1 pk ,not null

ID int primary key
or 
CREATE TABLE examp(
ID int not null,
primary key(ID)
);

Foreign key
column (set of columns) to refer pk in another table
can be multiple fks
can have duplicate and null values

CREATE TABLE dept (
  id int NOT NULL,
  name varchar(50),
  PRIMARY KEY (id)
);
CREATE TABLE teacher (
  id int NOT NULL,
  name varchar(50) ,
  dept_id int ,
  PRIMARY KEY (id)
  FOREIGN KEY (dept_id) REFERENCES dept (id)
  );

CASCADING for FK
ON UPDATE CASCADE
ON DELETE CASCADE

CREATE TABLE teacher (
  id int NOT NULL,
  name varchar(50) ,
  dept_id int ,
  PRIMARY KEY (id)
  FOREIGN KEY (dept_id) REFERENCES dept (id)
  ON UPDATE CASCADE
  ON DELETE CASCADE
  );


CREATE TABLE examp(
cust_id int,
foreign key (cust_id) references customer(id)
);

DEFAULT 
salary int DEFAULT 25000

Check
#it can limit values allowed in a column

CREATE TABLE license(
age INT CHECK (age>=18)
);
*/
/*
CREATE DATABASE school;
USE school;
CREATE TABLE student (
roll_no INT PRIMARY KEY,
name VARCHAR(50),
marks INT NOT NULL,
grade VARCHAR(1),
city VARCHAR(20)
);
INSERT INTO  student (roll_no,name,marks,grade,city) VALUES
(101,"anil",78,"C","delhi),
(102,"chetan",90,"A","mumbai");
*/
/* 
SELECT 
#to select data from the database(tables)
select col1,col2 from table_name; (only required columns)
select * from table_name;(all columns)

DISTINCT 
select distinct city from student;

WHERE clause
select col1,col2 from table_name where conditions;
select * from student where marks >80;

OPERATORS used with WHERE
Arithmetic operators: +,-,*,/,%
#select * from student where marks+10>100;
Comparison  operators: =,!=,>,<,>=,<=,
#select * from student where marks>85;
Logical  operators: AND ,OR ,NOT ,IN,BETWEEN,ALL,LIKE,ANY
AND(to check for both conditions to be true)
#select * from student where marks >80 AND city="delhi";
OR(to check for one of the conditions to be true)
#select * from student where marks >85 OR city="mumbai";
BETWEEN (selects for a given range)
#select * from student where marks BETWEEN 80 AND 90;
IN(matches any value in the list)
#select * from student where city IN ("delhi","mumbai");
NOT(to negate the given condition)
# select * from student where city NOT IN ("delhi");
Bitwise  operators: &(bitwise AND), |(bitwise OR)

LIMIT clause 
sets an upper limit on number of (tuples)rows to be returned
#select * from student LIMIT 1;
select col1,col2 from table_name LIMIT number;

ORDER BY clause
to sort in ascending (ASC) or descending order (DESC)
#select * from student order by city ASC;
#select * from student ORDER BY marks DESC LIMIT 2;
select col1,col2 from table_name ORDER BY col1 ASC;

Aggregate Functions
perform a calculation on a set of values  and return a single values
1.COUNT()
2.MAX()
3.MIN()
4.SUM()
5.AVG()
#select MAX(marks) from student;
#select MIN(marks) form student;
#select AVG(marks) from student;
#select COUNT(roll_no) from student;

GROUP BY clause
groups rows that have the same values into summary rows
it collects data from multiple records and groups the result by one or more column
generally we use group by with some aggregate function.

#select city,count(name) from student GROUP BY city;
#p1
select city ,avg(marks) 
from student 
group by city
order by  avg(marks);
#p2
select mode ,count(customer)
from payment
group by mode;

HAVING clause
applies some condition on rows
used when we want to apply any condition after grouping
# select count(name),city
from student 
group by city
HAVING max(marks)>85;

General order
SELECT column(s)
FROM table_name
WHERE condition
GROUP BY column(s)
HAVING condition
ORDER BY column(s);

UPDATE (to update existing rows)

UPDATE table_name 
SET col1=val2,col2=val2
WHERE condition;
#UPDATE student 
SET grade ="O"
WHERE grade="A";

SAFE MODE(UPDATES)
set sql_safe_updates=0; (off)
set sql_safe_updates=1; (on)

DELETE (to delete existing rows)
DELETE FROM table_name
WHERE condition;
#DELETE FROM student 
WHERE marks<90;

ALTER(to change the schema)

1.ADD column
ALTER TABLE table_name 
ADD COLUMN column_name datatype constraint;


2.DROP column
ALTER TABLE table_name 
DROP COLUMN column_name;

TRUNCATE (to delete table's data)(table exists)
TRUNCATE TABLE table_name

3.RENAME Table
ALTER TABLE table_name 
RENAME TO new_table_name;

4.CHANGE Column(rename)
ALTER TABLE table_name
CHANGE COLUMN old_name new_name new_datatype new_constraint;

5.MODIFY Column(modify datatype /constraint)
ALTER TABEL table_name
MODIFY col_name new_datatype new_constraint;

*/
/*
JOINS
used to combine rows from two or more tables, based on a related column between them
types of joins
1.INNER JOIN
returns records that have matching values in both tables
SYNTAX
SELECT column(s)
FROM table1
INNER JOIN table2
ON table1.col_name=table2.col_name;


OUTER JOIN
2.LEFT JOIN
returns all records from the left table,and the matched records from the right table
SYNTAX
SELECT column(s)
FROM table1 as t1
LEFT JOIN table2 as t2
ON t1.col_name=t2.col_name;

3.RIGHT JOIN
returns all records from the right table and the matched records from the left table
SYNTAX
SELECT column(s)
FROM table1 as t1
RIGHT JOIN table2
ON t1.col_name=t2.col_name;

4.FULL JOIN
returns all records when there is a match either left or right table
SYNTAX in MYSQL
SELECT * FROM student as s
LEFT JOIN course as c
ON s.id=c.id
UNION
SELECT * FROM student as s
RIGHT JOIN course as c
ON s.id=c.id;

SELF JOIN
SYNTAX
SELECT column(s)
FROM table as t1
Join table as t2
ON t1.col_name=t2.col_name;

LEFT EXCLUSIVE JOIN

SELECT column(s)
FROM table1 as t1
LEFT JOIN table2 as t2
ON t1.col_name=t2.col_name
WHERE t2.col_name IS NULL;

RIGHT EXCLUSIVE JOIN

SELECT column(s)
FROM table1 as t1
RIGHT JOIN table2 as t2
ON t1.col_name=t2.col_name
WHERE t1.col_name IS NULL;
*/