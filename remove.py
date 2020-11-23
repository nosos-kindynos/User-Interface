import pickle
from tkinter import *
#from main import admno

master = Tk()

master.geometry("300x600")
master.title('Contacts')

admno = input('Enter your admission no:')

filename=str(admno)+'.dat'

with open(filename,'rb') as f:
    existing = pickle.load(f)
    print(existing)

with open('data.dat','rb') as f:
    list = pickle.load(f)

old=existing[1][admno]

def update(old):
   for i in range(len(old)):
       if var[i].get()==1:
           old.pop(i)
   return old

def close():
    master.destroy()

Label(master, text="Remove contacts:").grid(row=0, sticky=W)

var = []

for i in range (len(old)):
    var.append(IntVar())

n=0
for i in list:
    if i[0] in old:
        Checkbutton(master, text=i[1], variable=var[n]).grid(row=n+1, sticky=W)
        n+=1

Button(master, text='Save', command=close).grid(row=n+1, sticky=W, pady=4)

mainloop()

existing[1][admno]=update(old)

with open(filename,'wb') as f:
   pickle.dump(existing,f)
