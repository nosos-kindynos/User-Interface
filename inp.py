from tkinter import *
from functools import partial
import csv

def close(admnoo):
    
    with open('master.csv','r') as f:
        admnoo=admnoo.get()
        reader=csv.reader(f)
        for row in reader:
            if not row==[] and row[0]==admnoo:
                master.destroy()
                if len(row)==2 or row[2] == '':
                    import trialregister
                else:
                    import login
                break
        else:
            messageLabel = Label(master, text="Admission number not found").grid(row=3, column=0)

master = Tk()
master.geometry('190x50') 
master.title("Welcome")

admnoLabel = Label(master, text="Adm number").grid(row=0, column=0,padx=10)
admnoo = StringVar()
admnoEntry = Entry(master, textvariable=admnoo,width=10).grid(row=0, column=1,padx=1)  

close=partial(close,admnoo)

enterButton = Button(master, text="Enter", command=close).grid(row=1 ,column=0,padx=10)

mainloop()


