import pickle
from tkinter import *
from functools import partial
#from main import admno

with open('data.dat','rb') as f:
    list = pickle.load(f)

master = Tk()  
master.geometry('300x100') 
master.title("Login")

admno=input('Enter your admission no: ')

def close(name,password):
    tup=(admno,name.get())
    if tup in list:
        filename=str(admno)+'.dat'
        with open (filename,'rb') as f:
            l=pickle.load(f)[0]
            if l['password']==password.get():
                master.destroy()
            else:
                messageLabel = Label(master, text="Login unsuccessful").grid(row=4, column=0)

    else:
        messageLabel = Label(master, text="Login unsuccessful").grid(row=4, column=0)
        
nameLabel = Label(master, text="Name").grid(row=0, column=0)
name = StringVar()
nameEntry = Entry(master, textvariable=name).grid(row=0, column=1)  

passwordLabel = Label(master,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(master, textvariable=password, show='*').grid(row=1, column=1)

close = partial(close, name, password)

registerButton = Button(master, text="Login", command=close).grid(row=3 ,column=0) 
