from tkinter import *
from addpeople import Addpeople
import sqlite3 #database 
from tkinter import messagebox
con=sqlite3.connect('database.db') # for connection 
cur=con.cursor() #for run queries

class Displaypeople(Toplevel):
    def __init__(self,id):
        self.id=id
        Toplevel.__init__(self)
        self.geometry("650x550+300+150")
        self.title("Display people")
        self.resizable(False,False)
        self.top=Frame(self,height=150,bg="white")#width=650)
        self.top.pack(fill=X)
        self.bottom=Frame(self,height=400,bg="#6286a6")
        self.bottom.pack(fill=X)
        #top frame design
        self.topimage=PhotoImage(file="icons/phonebook.png")
        self.toplabel=Label(self.top,image=self.topimage,bg="white")
        self.toplabel.place(x=60,y=25)
        self.heading=Label(self.top,text="Display people",font='arial 15 bold',bg="white",fg="orange")
        self.heading.place(x=210,y=45)
        
        query="select * from addressbook where person_id='{}'".format(id)
        result=cur.execute(query).fetchone()#or fetchall()
        print(result)
        person_name=result[1]
        person_mobileno=result[2]
        person_email=result[3]
        person_address=result[4]
        label1=Label(self.bottom,text=" Name ",font='arial 10 bold' )
        label1.place(x=40,y=20)
        label2=Label(self.bottom,text=" Mobile no. ",font='arial 10 bold' )
        label2.place(x=40,y=70)
        label3=Label(self.bottom,text=" Email ",font='arial 10 bold' )
        label3.place(x=40,y=120)
        label4=Label(self.bottom,text=" Address ",font='arial 10 bold' )
        label4.place(x=40,y=170)
        self.entry1=Entry(self.bottom,width=50,bd=5)
        self.entry1.place(x=200,y=20)
        self.entry1.insert(0,person_name)
        self.entry1.config(state="disabled")
        self.entry2=Entry(self.bottom,width=50,bd=5)
        self.entry2.place(x=200,y=70)
        self.entry2.insert(0,person_mobileno)
        self.entry2.config(state="disabled")
        self.entry3=Entry(self.bottom,width=50,bd=5)
        self.entry3.place(x=200,y=120)
        self.entry3.insert(0,person_email)
        self.entry3.config(state="disabled")
        self.entry4=Text(self.bottom,width=40,height=5,bd=5)
        self.entry4.place(x=200,y=170)
        self.entry4.insert(INSERT,person_address)
        self.entry4.config(state="disabled")