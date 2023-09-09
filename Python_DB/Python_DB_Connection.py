Step 1:
We will learn how to connect to the PostgreSQL database server in the Python program using the psycopg database adapter.

use the following command line from the terminal:

pip install psycopg2

Step2:

import psycopg2
hostname = 'localhost'
database = 'dvdrental'
username = 'postgres'
pwd = 'postgres'
port_id = 5432
conn = None
cur = None

try:
    conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id) 

    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS employee')
    create_script = '''CREATE TABLE employee(id int ,
                                            name varchar(40),
                                            salary int,
                                            dept_id varchar(30)) '''
          
    cur.execute(create_script)

    insert_script  = '''INSERT INTO employee  VALUES 
    (1,'Dinesh',12000,'D1'),
    (2,'Mahesh',15000,'D1'), 
    (3,'Satya',20000,'D2')'''
    cur.execute(insert_script)
    cur.execute('select * from employee')
    print(cur.fetchall())
    conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
        
------------------------------------------------------------------------
import psycopg2
hostname = 'localhost'
database = 'dvdrental'
username = 'postgres'
pwd = 'postgres'
port_id = 5432
conn = None
cur = None

try:
    conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id) 

    cur = conn.cursor()
    cur.execute('select * from employee')
    #print(cur.fetchall())
    for i in cur.fetchall(): # to print the data one by one
        print(i)
    conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
        
-------------------------------------------------------------------------
import psycopg2
hostname = 'localhost'
database = 'dvdrental'
username = 'postgres'
pwd = 'postgres'
port_id = 5432
conn = None
cur = None

try:
    conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id) 

    cur = conn.cursor()
    cur.execute('SELECT year,month,SUM (quantity) FROM sales GROUP BY CUBE (year, month) ORDER BY year, month')
    #print(cur.fetchall())
    for i in cur.fetchall(): # to print the data one by one
        print(i)
    conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()


-------------------------------------------------------------------------------------------
create table country_orders(
Country varchar(20),
Age varchar(10),
Salary varchar(10),
Purchased varchar(10)
);
insert into country_orders values
('France'	,'44',	'72000',	'No'),
('Spain'	,'27',	'48000',	'Yes'),
('Germany'	,'30',	'54000',	'No'  ),
('Spain'	,'38',	'61000',	'No');

insert into country_orders(Country, Age,Purchased) values('Germany','40','Yes');
insert into country_orders(Country, Salary,Purchased) values('Spain','52000','No');
insert into country_orders(Country, Salary,Purchased) values('Spain','52000','No');

insert into country_orders values
('France'	,'48',	'79000',	'Yes'),
('Germany'	,'50',	'83000',	'No'),
('France'	,'37',	'67000',	'Yes');

----------------------------------------------------------------------------------------
import psycopg2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

hostname = 'localhost'
database = 'dvdrental'
username = 'postgres'
pwd = 'postgres'
port_id = 5432
conn = None
cur = None

try:
    conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id) 

    cur = conn.cursor()
    cur.execute('SELECT Country,Age,Salary,Purchased from country_orders')
    dataset = cur.fetchall()
    data=np.array(dataset)
    #print(data[:, :-1])
    X = data[:, :-1]
    y = data[:, 3]  
    print(X)
    print(y)
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()





