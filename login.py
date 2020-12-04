from tkinter import *
from functools import partial
from main import admno
import csv

list=[]

with open('student_names.csv','r') as f:
    reader=csv.reader(f)
    for row in reader:
        if not row==[]:
            list.append(row)

master = Tk()  
master.geometry('300x100') 
master.title("Login")

def close(password):
##    tup=(admno,name.get())
##    if tup in list:
##        filename=admno+'.dat'
##        with open (filename,'rb') as f:
##            l=pickle.load(f)[0]
##            if l['password']==password.get():
##                master.destroy()
    
      with open ('master.csv','r') as f:
              reader=csv.reader(f)
              for row in reader:
                  if not row==[] and row[0]==admno:
                      if row[2]==password.get():
                          master.destroy()
                          import master_correction
                          import analysis
                          break
                
              else:
                  messageLabel = Label(master, text="Login unsuccessful").grid(row=4, column=0)

admnoLabel = Label(master, text="Adm no").grid(row=0, column=0)
temp=StringVar()
temp.set(admno)
admnoEntry = Entry(master,textvariable=temp)
admnoEntry.grid(row=0, column=1)
admnoEntry.config(state=DISABLED)

passwordLabel = Label(master,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(master, textvariable=password, show='*').grid(row=1, column=1)

close = partial(close, password)

registerButton = Button(master, text="Login", command=close).grid(row=3 ,column=0) 


