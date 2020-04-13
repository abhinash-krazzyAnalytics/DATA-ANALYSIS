# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 18:50:46 2020

@author: Abhinash
"""
#run port from xampp server mysql and apache

import pymysql
conn=pymysql.connect('localhost','root','','cms')
cur=conn.cursor()

while(True):
    print("-"*60)
    print(" @@@@@@@@  Welcome To Course Management System @@@@@@@@ ")
    print("-"*60)
    print()
    print("-------1:ADD Customer 2:MODIFY Customer-------")
    print("-------3:DEL Customer 4:Display Customer-------")
    print(" ")
    ch=int(input("Enter Choice :"))
    if(ch==1):
        idd=int(input("Enter New Id :"))
        name=str(input("Enter Name :"))
        cor=str(input("Enter Course :"))
        mob=str(input("Enter Mobile Number :"))
        fees=int(input("Enter Course Fees :"))
        q="insert into data(id,name,course,mob,fees) values(%s,%s,%s,%s,%s)"
        val=(idd,name,cor,mob,fees)
        cur.execute(q,val)
        conn.commit()
        print("--------Customer Added Sucessfully-------------------")
        print()
    elif(ch==2):
        idd=int(input("Enter Cutomer ID :"))
        i_find=(idd,)
        li=[]
        q="select id from data"
        cur.execute(q)
        for i in cur:
            li.append(i)
        if i_find in li :
            name=str(input("Enter New Name :"))
            cor=str(input("Enter Change Course :"))
            mob=str(input("Enter Mod Mobile :"))
            fees=int(input("Enter New Fees :"))
            q="update data set name=%s,course=%s,mob=%s,fees=%s where id=%s"#error
            val=(name,cor,mob,fees,i_find[0])
            cur.execute(q,val)
            conn.commit()
            print("-----------------Data Modify of Customer is Sucessfully --------------")
            print()
        else:
            print("Id Not Present In DataBase")
    elif(ch==3):
        idd=int(input("Enter Cutomer ID :"))
        i_find=(idd,)
        li=[]
        q="select id from data"
        cur.execute(q)
        for i in cur:
            li.append(i)
        if i_find in li :
            q="delete from data where id=%s"
            val=i_find[0]
            cur.execute(q,val)
            conn.commit()
            print("Account DELETED SUCESSFULLY")
            print()
        else:
            print("Id Not Present In DataBase")
            print()
    elif(ch==4):
         idd=int(input("Enter Cutomer ID :"))
         i_find=(idd,)
         li=[]
         q="select id from data"
         cur.execute(q)
         for i in cur:
             li.append(i)
         if i_find in li :
             Data=[]
             q="select * from data where id=%s"
             val=i_find[0]
             cur.execute(q,val)
             for i in cur:
                 Data.append(i)
                 d=Data[0]
                 #print("Id of customer is :",d[0])
                 print("Name of customer is :",d[1])
                 print("Course is :",d[2])
                 print("Mobile is :",d[3])
                 print("Fees is :",d[4])
             conn.commit()
             print()
         else:
             print("Id Not Present In DataBase")

    elif(ch==5):
        conn.close()
        break
    else:
        print("Invalid choice")


###############################################################################################
import pymysql
conn=pymysql.connect('localhost','root','','cms')
cur=conn.cursor()
q="select image from images where image_id=2"
cur.execute(q)
#error
from PIL import Image
# open method used to open different extension image file
im = Image.open(cur)
# This method will show image in any image viewer
im.show()

########################################################################################
# Python program showing
# abstract base class work

from abc import ABC, abstractmethod

class cal(ABC):
# abstract method
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        pass

class Addition(cal):
    # overriding abstract method
    def add(self):
        return a+b

a=6
b=6
# Driver code
addd =Addition(a,b)
print(addd.add())
######################################################################################

# Python program to
# demonstrate protected members


# Creating a base class
class Base:
	def __init__(self):

		# Protected member
		self._a = 2

# Creating a derived class
class Derived(Base):
	def __init__(self,b):
        self.b=b

		# Calling constructor of
		# Base class
		Base.__init__(self)
		print("Calling protected member of base class: ")
		print(self._a)


obj1 = Base()

# Calling protected member
# Outside class will result in
# AttributeError
print(obj1.a)

obj2 = Derived(5)
print(obj2._a)
print(obj2.show())


