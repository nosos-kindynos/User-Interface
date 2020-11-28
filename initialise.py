from tkinter import *
from tkinter import ttk
from main import admno
import csv

def update():
   
   dict={admno:[]}
   varint=[]
   closeval=[]
   
   for i in range(len(list)):
       if var[i].get()==1:
           if closearr[i].get()==0:
              closearr[i].set(5)
           dict[admno].append((list[i][0],closearr[i].get()))
           for j in radbut[i]:
                j.config(state=NORMAL)
       else:
          if not radbut[i]==0:
             for j in radbut[i]:
                j.config(state=DISABLED)
          closearr[i].set(0)
       varint.append(var[i].get())
       closeval.append(closearr[i].get())

   l=[]
   info=[]

   with open ('master.csv','r') as f:
              reader=csv.reader(f)
              for row in reader:
                  if not row==[] and row[0]==admno:
                      info.append(dict)
                      info.append(varint)
                      info.append(closeval)
                      row.append(info)
                  if not row == []:
                      l.append(row)

   with open ('master.csv','w') as f:
        writer=csv.writer(f)
        for i in l:
            if not i==[]:
               writer.writerow(i)


def close():

   master.destroy()

def getval(n):

   return var[n].get()


master = Tk()
master.title('Contacts')


main_frame = Frame(master)
main_frame.pack(fill=BOTH,expand=1)

my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

y_scrollbar = ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
y_scrollbar.pack(side=LEFT,fill=Y)

my_canvas.configure(yscrollcommand=y_scrollbar.set)
my_canvas.bind("<Configure>",lambda e: my_canvas.config(scrollregion= my_canvas.bbox(ALL))) 

second_frame = Frame(my_canvas)

my_canvas.create_window((0,0),window= second_frame, anchor="nw")

list=[]

with open('C:\\Users\\Sujal\\Downloads\\student_names.csv','r') as f:
    reader=csv.reader(f)
    for row in reader:
        if not row==[]:
            list.append(row)
       
Label(second_frame, text="Select your contacts:").grid(row=0)

var = []

closearr = []

for i in range (len(list)):
    var.append(IntVar())
    x=IntVar()
    x.set(0)
    closearr.append(x)

n=0

for i in list:
   
    if not i[0] == admno and not 'Name' in i[1]:       
        Checkbutton(second_frame, text=i[1], variable=var[n]).grid(row=n+1, column=0)
    n+=1

radbut=[]

n=0

for i in list:

   if not i[0]==admno and not 'Name' in i[1]:

        x=var[n].get()

        Rb1 = Radiobutton(second_frame, text = "", variable = closearr[n], value = 5)#.grid(row=n+1,column=1)
        Rb1.grid(row=n+1,column=1)
##        if x==0:
##              Rb1.config(state=DISABLED)
        Rb2 = Radiobutton(second_frame, text = "", variable = closearr[n], value = 10)#.grid(row=n+1,column=2)
        Rb2.grid(row=n+1,column=2)
##        if x==0:
##              Rb2.config(state=DISABLED)
        Rb3 = Radiobutton(second_frame, text = "", variable = closearr[n], value = 15)#.grid(row=n+1,column=3)
        Rb3.grid(row=n+1,column=3)
##        if x==0:
##              Rb3.config(state=DISABLED)

        radbut.append((Rb1,Rb2,Rb3))

   else:

      radbut.append(0)

   n+=1
           
Button(second_frame, text='Save', command=update).grid(row=n+1,column=0)

Button(second_frame, text='Quit', command=close).grid(row=n+1,column=1)

mainloop()

