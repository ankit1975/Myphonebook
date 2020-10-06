from tkinter import *
class Mypeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x550+300+150")
        self.title("My People")
        self.resizable(False,False)
        self.top=Frame(self,height=150,bg="white")#width=650)
        self.top.pack(fill=X)
        self.bottom=Frame(self,height=400,bg="#2fa0bc",width=650)
        self.bottom.pack()
        #top frame design
        self.topimage=PhotoImage(file="icons/phonebook.png")
        self.toplabel=Label(self.top,image=self.topimage,bg="white")
        self.toplabel.place(x=60,y=25)
        self.heading=Label(self.top,text="My people",font='arial 15 bold',bg="white",fg="orange")
        self.heading.place(x=210,y=45)
        self.sbframe=Frame(self.bottom,height=400,width=150,bg="#377a9b")
        self.sbframe.place(x=500,y=0)
        self.addbutton=Button(self.sbframe,text=" add ",width=10)
        self.addbutton.place(x=30,y=30)
        self.updatebutton=Button(self.sbframe,text=" update ",width=10)
        self.updatebutton.place(x=30,y=80)
        self.deletebutton=Button(self.sbframe,text=" delete ",width=10)
        self.deletebutton.place(x=30,y=130)
        #list box

        #self.listbox=Listbox(self.bottom,width=30,height=5)
        #self.listbox.grid(row=0,column=0)
        """self.scroll=Scrollbar(self.bottom,command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0,column=1,fill=Y)

        
"""
        

        
        
