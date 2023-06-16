import tkinter as tk
from datetime import datetime
import json
import mysql.connector as sql
from StockEntry import StockEntry
mytab=sql.connect(host='localhost',user='root',passwd='26012004',database='storestockrecord')
o1=mytab.cursor()
d1iq={}# items quantity in stock dict
d2ip={}#items price dict
w1=tk.Tk()#window 1 main window at start
w1.title('Main Store Interface')
w1.geometry('700x700')
t1=tk.Label(w1,text='Welcome To The Main Store Interface',font=('Arial Bold',28),fg='Blue')#text1
t1.grid(column=16,row=1)
b1=tk.Button(w1,text='Stock Entry',fg='red',font=('Arial Bold',22),width=16,height=5,command=Stock_Entry)#button1
b1.grid(column=16,row=3)
