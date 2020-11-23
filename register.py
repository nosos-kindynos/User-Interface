import pickle
from tkinter import *
from functools import partial
#from main import admno

admno=input('Enter your admission number: ')

def close(name,password):
    tup=(admno,name.get())
    if tup in list:
        filename=str(admno)+'.dat'
        with open (filename,'wb') as f:
            pickle.dump([{'password':password.get()}],f)    
        master.destroy()
    else:
        messageLabel = Label(master, text="Registration unsuccessful").grid(row=4, column=0)

e=input('Enter to continue: ')
  
with open('data.dat','rb') as f:
    list = pickle.load(f)

master = Tk()
master.geometry('300x100') 
master.title("Register")

nameLabel = Label(master, text="Name").grid(row=0, column=0)
name = StringVar()
nameEntry = Entry(master, textvariable=name).grid(row=0, column=1)  

passwordLabel = Label(master,text="Password").grid(row=2, column=0)  
password = StringVar()
passwordEntry = Entry(master, textvariable=password, show='*').grid(row=2, column=1)

close=partial(close, name, password)

registerButton = Button(master, text="Register", command=close).grid(row=3 ,column=0)
