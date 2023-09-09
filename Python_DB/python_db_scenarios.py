import psycopg2
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

    cur.execute('DROP TABLE IF EXISTS employee1')
    create_script = '''CREATE TABLE if not exists employee1(id int ,
                                            name varchar(40),
                                            salary int,
                                            dept_id varchar(30),
                                            branch varchar(32),
                                            account_Number varchar(32),
                                            Transaction_id int,
                                            Transaction_status varchar(42),
                                            Transaction_limit  int,
                                            Transaction_year int,
                                            Transaction_month varchar(21),
                                            Transaction_day varchar(32),
                                            Transaction_hour int) '''
        
            
    cur.execute(create_script)
    insert_script = '''insert into employee1(id,name,salary,dept_id,branch,account_Number,Transaction_id,Transaction_status,Transaction_limit,Transaction_year,Transaction_month,Transaction_day,Transaction_hour) 
    values (101,'James', 12000, 'D1',NULL,'SBI00123',10235,'successful',50000,2022,'may','monday',10),
    (102,'suresh', 25000, 'D1','secunderabad','SBI00133',10205,'unsuccessful',15000,2021,'september','tuesday',06),
    (103,'raju', Null, 'D2','boduppal','SBI00122',10265,'successful',25000,2022,'augest','sunday',15),
    (104,'rani', 65000, 'D3','ramanthapur','SBI00165',10005,'successful',90000,2022,'july','wednesday',18),
    (105,'mahesh', 35000, 'D6','amberpet','SBI00135',10665,'unsuccessful',10000,2021,'june','monday',Null),
    (106,'ganesh', 62000, Null,'begumpet','SBI00178',10465,'None',30000,2022,'april','friday',02)'''
    cur.execute(insert_script)
    cur.execute('select * from employee1')
    data = cur.fetchall()

    df1 = pd.DataFrame(data=data,columns=['id','name','salary','dept_id','branch','account_Number','Transaction_id','Transaction_status','Transaction_limit','Transaction_year','Transaction_month','Transaction_day','Transaction_hour'])
    #print(df1)
    print(df1.isna().sum())
    print(df1.isna().mean())
    
    cur.execute('''SELECT avg(Transaction_hour),Transaction_day FROM employee1
    group by Transaction_day''')
    data = cur.fetchall()
    conn.commit() 
    df = pd.DataFrame(data=data,columns=['hour','day'])
    print(df)
   

except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()


---------------------------------------------------
df1.info()

---------------------------------------------------
subset = ['salary', 'Transaction_hour']
df1.loc[:, subset] = df1.loc[:, subset].fillna(0)
df1
------------------------------------------------------
df1.fillna("NA",inplace=True)
df1.head()
-----------------------------------------------------------------------------------
df = pd.DataFrame(data=data,columns=['Transaction_hours','Transaction_day'])
df.plot.scatter(x='Transaction_hours', y='Transaction_day')
------------------------------------------------------------------------------------
