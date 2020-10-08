from tkinter import *
from addpeople import Addpeople
from updatepeople import Updatepeople
import sqlite3 #database 
from tkinter import messagebox
from displaypeople import Displaypeople
con=sqlite3.connect('database.db') # for connection 
cur=con.cursor() #for run queries

class Mypeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x550+300+150")
        self.title("My People")
        self.resizable(False,False)
        self.top=Frame(self,height=150,bg="white")#width=650)
        self.top.pack(fill=X)
        self.bottom=Frame(self,height=400,bg="#2fa0bc")
        self.bottom.pack(fill=X)
        #top frame design
        self.topimage=PhotoImage(file="icons/phonebook.png")
        self.toplabel=Label(self.top,image=self.topimage,bg="white")
        self.toplabel.place(x=60,y=25)
        self.heading=Label(self.top,text="My people",font='arial 15 bold',bg="white",fg="orange")
        self.heading.place(x=210,y=45)
        #buttons
        self.sbframe=Frame(self.bottom,height=400,width=150,bg="#377a9b")
        self.sbframe.place(x=500,y=0)
        self.addbutton=Button(self.sbframe,text=" add ",width=10,command=self.addpeople)
        self.addbutton.place(x=30,y=30)
        self.updatebutton=Button(self.sbframe,text=" update ",width=10,command=self.update)
        self.updatebutton.place(x=30,y=80)
        self.displaybutton=Button(self.sbframe,text=" display ",width=10,command=self.display)
        self.displaybutton.place(x=30,y=130)
        self.deletebutton=Button(self.sbframe,text=" delete ",width=10,command=self.delete)
        self.deletebutton.place(x=30,y=180)
        #list box
        self.listbox=Listbox(self.bottom,width=40,height=25)
        self.listbox.grid(row=0,column=0,padx=(40,0))
        self.scroll=Scrollbar(self.bottom,command=self.listbox.yview,orient=VERTICAL)
        self.listbox.config(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0,column=1,sticky=N+S)
        persons=cur.execute("select * from addressbook")
        r=persons.fetchall()
        print(r)
        count=0
        for i in r:
            self.listbox.insert(count,str(i[0])+" : "+i[1]+" " +str(i[2]))
            count+=1
    def addpeople(self):
        add=Addpeople()
        self.destroy()
    def update(self):
        selecteditem=self.listbox.curselection()
        print(selecteditem)
        person=self.listbox.get(selecteditem)
        print(person)
        personid=person.split(":")[0]
        print(personid)
        update=Updatepeople(personid)
    def display(self):
        selecteditem=self.listbox.curselection()
        print(selecteditem)
        person=self.listbox.get(selecteditem)
        print(person)
        personid=person.split(":")[0]
        print(personid)
        display=Displaypeople(personid)
    def delete(self):
        selecteditem=self.listbox.curselection()
        #print(selecteditem)
        person=self.listbox.get(selecteditem)
        #print(person)
        personid=person.split(":")[0]
        #print(personid)
        #display=Displaypeople(personid)
        query="delete from addressbook where person_id={}".format(personid)
        answer=messagebox.askquestion("warning!!!","are you sure you want to delete this contact ? ")
        if answer=="yes":
            try:
                cur.execute(query)
                con.commit()
                messagebox.showinfo("success","contact deleted ")
            except Exception as e:
                print(e)




        
     

        
        
