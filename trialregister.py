from tkinter import *
from functools import partial
from main import admno
import csv

#admno=input('Enter your admission number: ')

def close(password):
    l=[]
    if not password.get()=='':
      with open ('master.csv','r') as f:
              reader=csv.reader(f)
              for row in reader:
                  if not row==[] and row[0]==admno:
                      row.append(password.get())
                  if not row == []:
                      l.append(row)
      with open ('master.csv','w') as f:
          writer=csv.writer(f)
          for i in l:
              if not i==[]:
                  writer.writerow(i)
      master.destroy()
      import initialise
    else:
        messageLabel = Label(master, text="Registration unsuccessful").grid(row=4, column=0)

list=[]

with open('student_names.csv','r') as f:
    reader=csv.reader(f)
    for row in reader:
        if not row==[]:
            list.append(row)

master = Tk()
master.geometry('300x100') 
master.title("Register")

admnoLabel = Label(master, text="Adm no").grid(row=0, column=0)
temp=StringVar()
temp.set(admno)
admnoEntry = Entry(master,textvariable=temp)
admnoEntry.grid(row=0, column=1)
admnoEntry.config(state=DISABLED)

passwordLabel = Label(master,text="Password").grid(row=2, column=0)  
password = StringVar()
passwordEntry = Entry(master, textvariable=password, show='*').grid(row=2, column=1)

close=partial(close, password)

registerButton = Button(master, text="Register", command=close).grid(row=3 ,column=0)
