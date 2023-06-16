import mysql.connector as sql
mytab=sql.connect(host='localhost',user='root',passwd='26012004',database='storestockrecord')
o1=mytab.cursor()
c1='CREATE TABLE EMPFB(ECODE char(6),EmpName varchar(30),Passwd char(6));'
o1.execute(c1)
mytab.commit()
s=[('AB1507','Aman','BA7015'),('WD1908','Owais','DW8019'),('FN2204','Hari','NF4022')]
for i in range(len(s)):
    c2="INSERT INTO empfb(ECODE,EmpName,Passwd) VALUES('{}','{}','{}')".format(s[i][0],s[i][1],s[i][2])
    o1.execute(c2)
mytab.commit()
