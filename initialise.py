import pickle
from tkinter import *
#from main import admno

def update(admno):
   dict={admno:[]}
   for i in range(len(list)):
       if var[i].get()==1:
           dict[admno].append(list[i][0])
   return dict

def close():
    master.destroy()

admno=input('Enter your admission no: ')

master = Tk()

master.geometry("300x600")
master.title('Contacts')

with open('data.dat','rb') as f:
    list = pickle.load(f)
       
Label(master, text="Select your contacts:").grid(row=0, sticky=W)

var = []

for i in range (len(list)):
    var.append(IntVar())

n=0
for i in list:
    if not i[0] == admno:
        Checkbutton(master, text=i[1], variable=var[n]).grid(row=n+1, sticky=W)
##    else:
##        var[n]=='same'
    n+=1

Button(master, text='Save', command=close).grid(row=n+1, sticky=W, pady=4)

mainloop()

contacts=[]
contacts.append(update(admno))

print(contacts)

filename=admno+'.dat'

with open(filename,'ab') as f:
   pickle.dump(contacts,f)

