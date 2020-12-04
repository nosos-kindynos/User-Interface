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
              closearr[i].set(0.33)
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
                      row=row[0:3]
                      row.append(info)
                  if not row == []:
                      l.append(row)

   with open ('master.csv','w') as f:
        writer=csv.writer(f)
        for i in l:
            if not i==[]:
               #print(i)
               writer.writerow(i)


def close():

   master.destroy()
   import master_correction
   import analysis
   
master = Tk()
master.title('Contacts')

main_frame = Frame(master)
main_frame.pack(fill=BOTH,expand=1)

my_canvas = Canvas(main_frame)
my_canvas.pack(side=RIGHT,fill=BOTH,expand=1)

y_scrollbar = ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
y_scrollbar.pack(side=RIGHT,fill=Y)

my_canvas.configure(yscrollcommand=y_scrollbar.set)
my_canvas.bind("<Configure>",lambda e: my_canvas.config(scrollregion= my_canvas.bbox(ALL))) 

second_frame = Frame(my_canvas)

my_canvas.create_window((0,0),window= second_frame, anchor="nw")

list=[]
name=''

with open('student_names.csv','r') as f:
    reader=csv.reader(f)
    for row in reader:
        if not row==[]:
            list.append(row)
        if row[0]==admno:
            name=row[1]
       
Label(second_frame, text="Select your contacts,"+name).grid(row=0,sticky=W)

var = []

closearr = []

for i in range (len(list)):
    var.append(IntVar())
    x=DoubleVar()
    x.set(0)
    closearr.append(x)

n=0
radbut=[]

for i in list:
   
    if not i[0] == admno and not 'Name' in i[1]:       
        
        x=var[n].get()

        Label(second_frame, text="").grid(row=n+1,column=0,sticky=W)

        Rb1 = Radiobutton(second_frame, text = "", variable = closearr[n], value = 0.33)#.grid(row=n+1,column=1)
        Rb1.grid(row=n+1,column=1)
##        if x==0:
##              Rb1.config(state=DISABLED)
        Rb2 = Radiobutton(second_frame, text = "", variable = closearr[n], value = 0.67)#.grid(row=n+1,column=2)
        Rb2.grid(row=n+1,column=2)
##        if x==0:
##              Rb2.config(state=DISABLED)
        Rb3 = Radiobutton(second_frame, text = "", variable = closearr[n], value = 1.0)#.grid(row=n+1,column=3)
        Rb3.grid(row=n+1,column=3)
##        if x==0:
##              Rb3.config(state=DISABLED)
        Rb4 = Radiobutton(second_frame, text = "", variable = closearr[n], value = 1.33)#.grid(row=n+1,column=3)
        Rb4.grid(row=n+1,column=4)

        Rb5 = Radiobutton(second_frame, text = "", variable = closearr[n], value = 1.67)#.grid(row=n+1,column=3)
        Rb5.grid(row=n+1,column=5)
 
        radbut.append((Rb1,Rb2,Rb3,Rb4,Rb5))

        Checkbutton(second_frame, text=i[1], variable=var[n],command=update).grid(row=n+1, column=0,sticky=W)

    else:

      radbut.append(0)

    n+=1
           
Button(second_frame, text='Save', command=update).grid(row=n+1,column=0)

Button(second_frame, text='Quit', command=close).grid(row=n+1,column=1)

mainloop()

