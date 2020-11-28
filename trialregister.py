import pickle
from tkinter import *
from functools import partial
from main import admno
import csv

#admno=input('Enter your admission number: ')

def close(name,password):
    x=name.get()
    x='  '+x+'  '
    rec=[admno,x]
    l=[]
    if rec in list:
      with open ('master.csv','r') as f:
              reader=csv.reader(f)
              for row in reader:
                  if row==rec:
                      row.append(password.get())
                  if not row == []:
                      l.append(row)
      with open ('master.csv','w') as f:
          writer=csv.writer(f)
          for i in l:
              if not i==[]:
                  writer.writerow(i)
      master.destroy()
      e=input('Proceed?')
      import initialise
    else:
        messageLabel = Label(master, text="Registration unsuccessful").grid(row=4, column=0)

e=input('Enter to continue: ')
  
list=[]

with open('C:\\Users\\Sujal\\Downloads\\student_names.csv','r') as f:
    reader=csv.reader(f)
    for row in reader:
        if not row==[]:
            list.append(row)

#print(list)

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
