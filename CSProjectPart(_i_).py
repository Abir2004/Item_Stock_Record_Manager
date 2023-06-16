import mysql.connector as sql
mydb=sql.connect(host='localhost',user='root',passwd='26012004')
o1=mydb.cursor()#Object 1
c1='CREATE DATABASE StoreStockRecord'
o1.execute(c1)
c2='USE StoreStockRecord'
o1.execute(c2)
c3='CREATE TABLE StockEntry(ItemName varchar(30) PRIMARY KEY,Price FLOAT,Quantity int)'
o1.execute(c3)
mydb.commit()
