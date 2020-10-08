from tkinter import *
import datetime
from mypeople import Mypeople
from addpeople import Addpeople
from updatepeople import Updatepeople
from aboutus import Aboutus
date=datetime.datetime.now().date()
date=str(date)

class Application(object):
    def __init__(self,master):
        self.m=master
        #frames
        self.top=Frame(self.m,height=150,bg="white")#width=650)
        self.top.pack(fill=X)
        self.bottom=Frame(master,height=400,bg="#2fa0bc",width=650)
        self.bottom.pack()
        #top frame design
        self.topimage=PhotoImage(file="icons/phonebook.png")
        self.toplabel=Label(self.top,image=self.topimage,bg="white")
        self.toplabel.place(x=60,y=25)
        self.heading=Label(self.top,text="My Phone Book App",font='arial 15 bold',bg="white",fg="orange")
        self.heading.place(x=210,y=45)
        self.datelabel=Label(self.top,text="today's date: "+date,font='arial 12 bold',fg="blue",bg="white")
        self.datelabel.place(x=450,y=10)
        #adding button in bottom frame
        self.viewbutton=Button(self.bottom,text="  My people  ",width=15,fg="#219991",command=self.mypeople)
        self.viewbutton.place(x=250,y=50)
        self.addbutton=Button(self.bottom,text="  Add people  ",width=15,fg="#219991",command=self.addpeople)
        self.addbutton.place(x=250,y=100)
        self.aboutbutton=Button(self.bottom,text="  About us  ",width=15,fg="#219991",command=self.about)
        self.aboutbutton.place(x=250,y=150)
    def mypeople(self):
        people=Mypeople()
    def addpeople(self):
        add=Addpeople()
    def about(self):
        about=Aboutus()


def main():
    root=Tk()
    app=Application(root)
    root.title("phoneBook")
    root.geometry("650x550+300+150")
    root.resizable(False,False)
    root.mainloop()


if __name__=='__main__':
    main()
