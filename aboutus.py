from tkinter import *
class Aboutus(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x550+300+150")
        self.title("About us")
        self.resizable(False,False)
        self.top=Frame(self,height=150,bg="white")#width=650)
        self.top.pack(fill=X)
        self.bottom=Frame(self,height=400,bg="#2fa0bc")
        self.bottom.pack(fill=X)
        #top frame design
        self.topimage=PhotoImage(file="phonebook.png")
        self.toplabel=Label(self.top,image=self.topimage,bg="white")
        self.toplabel.place(x=60,y=25)
        self.heading=Label(self.top,text="About us",font='arial 15 bold',bg="white",fg="orange")
        self.heading.place(x=210,y=45)
        self.label=Label(self.bottom,text=" Hiiii this Phonebook Application is made with Tkinter Module" 
        "\n connect with us " "\n linkedin : https://www.linkedin.com/in/ankit-malpani-7b2a07191/" 
        "\n github   : https://github.com/ankit1975" 
        " \n instagram:https://www.instagram.com/maheshwari.99/",font= 'arial 12 bold' ,bg="#2fa0bc",fg="white",height=400)
        self.label.pack(fill=Y)
