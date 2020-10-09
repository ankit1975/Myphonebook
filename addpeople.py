from tkinter import *
from tkinter import messagebox
import sqlite3
con=sqlite3.connect('database.db')
cur=con.cursor()
class Addpeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x550+300+150")
        self.title("View People")  
        self.resizable(False,False)
        self.top=Frame(self,height=150,bg="white")#width=650)
        self.top.pack(fill=X)
        self.bottom=Frame(self,height=400,bg="#a5e038")
        self.bottom.pack(fill=BOTH)
        #top frame design
        self.topimage=PhotoImage(file="phonebook.png")
        self.toplabel=Label(self.top,image=self.topimage,bg="white")
        self.toplabel.place(x=60,y=25)
        self.heading=Label(self.top,text="Add people",font='arial 15 bold',bg="white",fg="#d56ce2")
        self.heading.place(x=210,y=45)
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
        self.entry1.insert(0,"enter name")
        self.entry2=Entry(self.bottom,width=50,bd=5)
        self.entry2.place(x=200,y=70)
        self.entry2.insert(0,"enter mobile no.")
        self.entry3=Entry(self.bottom,width=50,bd=5)
        self.entry3.place(x=200,y=120)
        self.entry3.insert(0,"enter email")
        self.entry4=Text(self.bottom,width=40,height=5,bd=5)
        self.entry4.place(x=200,y=170)
        self.entry4.insert(INSERT,"enter address")
        button=Button(self.bottom,text="submit",bg="#3587b7",width=15,command=self.addpeople)
        button.place(x=220,y=360)
    def addpeople(self):
        name=self.entry1.get()
        mobileno=self.entry2.get()
        email=self.entry3.get()
        address=self.entry4.get(1.0,'end-1c')
        #print(name)
        if name and mobileno and email and address != "":
            try:
                #create table
                query="""CREATE TABLE addressbook(
                                    person_id integer PRIMARY KEY,
                                    person_name text NOT NULL,
                                    person_mobileno integer,
                                    person_email text NOT NULL,
                                    person_address text NOT NULL);"""
                cur.execute(query)
                con.commit()
                #insert into database 
                query="insert into 'addressbook'(person_name,person_mobileno,person_email,person_address) values(?,?,?,?)"
                cur.execute(query,(name,mobileno,email,address))
                con.commit()
                messagebox.showinfo("success","contact added")
            except EXCEPTION as e:
                messagebox.showerror("Error",str(e))
        else:

            #print("abe sale")
            messagebox.showerror("error","Abe Sale ,Maaf krna kabhi idhar udhr nikal jata hu🤣,Please fill all fields !!!",icon="warning")


          

