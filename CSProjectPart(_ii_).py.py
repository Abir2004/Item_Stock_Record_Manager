import tkinter as tk
from datetime import datetime
import json
import mysql.connector as sql
mytab=sql.connect(host='localhost',user='root',passwd='26012004',database='storestockrecord')
o1=mytab.cursor()
d1iq={}# items quantity in stock dict
d2ip={}#items Wholesale cost dict
d3ip={}#items sell price dict
w1=tk.Tk()#window 1 main window at start
w1.title('Main Store Interface')
w1.geometry('700x700')
t1=tk.Label(w1,text='Welcome To The Main Store Interface',font=('Arial Bold',28),fg='Blue')#text1
t1.grid(column=16,row=1)
def Stock_Entry():#StockEntry Command1
    n1=0
    global w2
    w2=tk.Tk()#window 2 for stock entry
    w2.geometry('600x600')
    def INSERT():
        z1,z2,z3,z4=i1.get(),p1.get(),q1.get(),p2.get()
        c1="INSERT INTO stockentry(ItemName,WholeSaleCost,SalePrice,Quantity) VALUES('{}',{},{},{})".format(z1,z2,z4,z3)#sqlcommand1
        o1.execute(c1)
        c2='SELECT ItemName,WholeSaleCost,SalePrice,Quantity FROM stockentry'#sqlcommand3
        o1.execute(c2)
        for i in o1:
            d2ip[i[0]]=i[1]
            d1iq[i[0]]=i[3]
            d3ip[i[0]]=i[2]
        n1=len(d1iq)#change in item number
        s1=str(n1)+' items have been registered'
        s2=json.dumps(d1iq,indent=2)#pretty printing
        mytab.commit()
        quit(w3)
        quit(w2)
    def quit(self):
        self.destroy()
    def Enter():
        global w3
        w3=tk.Tk()#window3
        w3.title('Confirmation')
        w3.geometry('600x150')
        t6=tk.Label(w3,text='Are you Sure you want to Continue',font=('Arial Bold',18))#text6
        t6.grid(column=4,row=0)
        b3=tk.Button(w3,text='Yes',fg='blue',width=7,height=3,command=INSERT)#button3
        b3.grid(column=3,row=1)
        b4=tk.Button(w3,text='No',fg='blue',width=7,height=3,command=lambda:[quit(w3)])#button4
        b4.grid(column=5,row=1)
        w3.mainloop()
        w2.mainloop()
    w2.title('Stock Entry')
    t2=tk.Label(w2,text='Enter Item Name:',font=('Arial Bold',18))#text2
    t2.grid(column=0,row=2)
    i1=tk.Entry(w2,width=20,bg='yellow')#item entry1 dabba1
    i1.grid(column=1,row=2)
    t3=tk.Label(w2,text='Enter Wholesale Cost:',font=('Arial Bold',18))#text3
    t3.grid(column=0,row=4)
    p1=tk.Entry(w2,width=10,bg='yellow')#Wholesale cost of item entry dabba2
    p1.grid(column=1,row=4)
    t7=tk.Label(w2,text='Enter Sale Price:',font=('Arial Bold',18))#text7
    t7.grid(column=0,row=6)
    p2=tk.Entry(w2,width=10,bg='yellow')#Sale price of item entry dabba4
    p2.grid(column=1,row=6)
    t4=tk.Label(w2,text='Enter Quantity:',font=('Arial Bold',18))#text4
    t4.grid(column=0,row=8)
    q1=tk.Entry(w2,width=10,bg='yellow')#quantity entry dabba3
    q1.grid(column=1,row=8)
    t5=tk.Label(w2,text='Press Enter to Continue',font=('Arial Bond',18))#text5
    t5.grid(column=6,row=8)
    b2=tk.Button(w2,text='Enter',fg='blue',width=10,height=3,command=Enter)#button 2
    b2.grid(column=6,row=9)
def Stock_Details():#Stock_Details Command2
    c3='Select ItemName,Quantity,WholeSaleCost,SalePrice FROM stockentry'#command3
    o1.execute(c3)
b1=tk.Button(w1,text='Stock Entry',fg='red',font=('Arial Bold',22),width=16,height=5,command=Stock_Entry)#button1
b1.grid(column=16,row=3)
b5=tk.Button(w1,text='Stock Details',fg='red',font=('Arial Bold',22),width=16,height=5,command=Stock_Details)#button1
b5.grid(column=16,row=5)
