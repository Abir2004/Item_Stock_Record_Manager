import mysql.connector as sql
mytab=sql.connect(host='localhost',user='root',passwd='26012004',database='storestockrecord')
curse=mytab.cursor()
curse.execute('CREATE TABLE BillDet(BillNo int,Dt Date,SalesmanName varchar(20),CustomerName varchar(20),PhoneNumber varchar(10))')
mytab.commit()
