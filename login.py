from tkinter import *
from functools import partial
from main import admno
import csv

list=[]

with open('C:\\Users\\Sujal\\Downloads\\student_names.csv','r') as f:
    reader=csv.reader(f)
    for row in reader:
        if not row==[]:
            list.append(row)

master = Tk()  
master.geometry('300x100') 
master.title("Login")

def close(name,password):
##    tup=(admno,name.get())
##    if tup in list:
##        filename=admno+'.dat'
##        with open (filename,'rb') as f:
##            l=pickle.load(f)[0]
##            if l['password']==password.get():
##                master.destroy()
    x=name.get()
    x='  '+x+'  '
    rec=[admno,x]
    l=[]
    if rec in list:
      with open ('master.csv','r') as f:
              reader=csv.reader(f)
              for row in reader:
                  if row[0:2]==rec:
                      if row[2]==password.get():
                          master.destroy()
                          e=input('Proceed?')
                          import trialupdate
                
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


