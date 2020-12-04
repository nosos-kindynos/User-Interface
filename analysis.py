from tkinter import *
from tkinter import ttk
#from master_correction import analysed_data
#from master_correction import person
from main import admno
from modelling import *
from risk_estimation import *
from functions import *
import csv

c=0
master = Tk()

def update():

    master.destroy()
    master.__init__()

    def update1():
       
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
                   writer.writerow(i)


    def close1():
       master.destroy()
       master.__init__()
       create()

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

    with open('student_names.csv','r') as f:
        reader=csv.reader(f)
        for row in reader:
            if not row==[]:
                list.append(row)
             
           
    Label(second_frame, text="Select your contacts:").grid(row=0,sticky=W)

    with open ('master.csv','r') as f:
              reader=csv.reader(f)
              for row in reader:
                  if not row==[] and row[0]==admno:
                      #print(row[-1])
                      a=eval(row[3])
                      refvarint=a[1]
                      refcloseval=a[2]

    var = []
    closearr = []

    for i in range (len(list)):
        x=IntVar()
        x.set(refvarint[i])
        var.append(x)
        y=DoubleVar()
        y.set(refcloseval[i])
        closearr.append(y)

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

            Checkbutton(second_frame, text=i[1], variable=var[n],command=update1).grid(row=n+1, column=0,sticky=W)

        else:

          radbut.append(0)

        n+=1
               
    Button(second_frame, text='Save', command=update1).grid(row=n+1,column=0)

    Button(second_frame, text='Quit', command=close1).grid(row=n+1,column=1)

    mainloop()

def toggle():

   master.destroy()

   lx=[]
   
   with open('master.csv','r') as f:
    reader=csv.reader(f)
    for row in reader:
        if not row==[] and row[0]==admno:
           if not row[1].endswith('*'):
              row[1]=row[1]+'*'
           else:
              row[1]=row[1][0:-1]
        if not row==[] and not row==['','']:
            lx.append(row)

   with open('master.csv','w') as f:
    writer=csv.writer(f)
    for i in lx:
        if not i==[] and not i==['','']:
           writer.writerow(i)

   #import master_correction
   
   master.__init__()
   create()
   
def create():

   master.title('Analysis')

   accuracy=2
   average_transfer_chance=0.14
   top_num_of_paths=10

   sources=[]

   with open('master.csv','r') as f:
       reader=csv.reader(f)
       for row in reader:
           if not row==[]:
              if row[1].endswith('*'):
                 sources.append(int(row[0]))


   data=read('master.csv')
   people_who_filled_data=data[0]
   filled_data=data[1]

   mapping = model_data_to_weighted_dyadic_relationships(average_transfer_chance, filled_data)
   list_of_first_degree_connections=mapping[0]
   risk_mapping=mapping[1]
   full_analysis={}

   people=mapping[2]

   for person in people:

       if person not in sources:
           
           risk=[]
           contacts_risk = []
           paths = {}

           relative_mapping = relative_map(None,[person],list_of_first_degree_connections)
           contacts=list_of_first_degree_connections.get(person)

           for contact in contacts:
               analysis=estimate_risk( sources , contact , relative_mapping  , risk_mapping ,accuracy , top_num_of_paths)
               posed_risk=analysis[0]*(get_risk((contact,person),risk_mapping))
               contacts_risk.append((contact,posed_risk))
               risk.append(posed_risk)
               paths.update({contact:analysis[1]})
           

           net_risk=union(risk)
           analysed_data=[net_risk, contacts_risk ]
           full_analysis.update({person:analysed_data})


   di={}
   for i in people:
       di.update({i:[]})
   for i in full_analysis:
       for j in full_analysis.get(i)[1]:
           k=di.get(j[0])
           k.append((i,j[1]))
           di.update({j[0]:k})


   write(people,full_analysis,di,'master.csv',sources)


   l=[]
   name=''

   with open('master.csv','r') as f:
       reader=csv.reader(f)
       for row in reader:
           if not row==[] and row[0]==admno:
              l=eval(row[4])
              name=row[1]
              break

   if len(l)==1:
      l.insert(0,[])
      l.insert(0,1)

   main_frame = Frame(master)
   main_frame.pack(fill=BOTH,expand=0)

   Label(main_frame, text="Your risk is currently:"+str(l[0]))

   my_canvas = Canvas(main_frame)
   my_canvas.pack(side=LEFT,fill=BOTH,expand=0)
   frame1 = Frame(my_canvas)

   my_canvas2 = Canvas(main_frame)
   my_canvas2.pack(side=RIGHT,fill=BOTH,expand=0)
   frame2 = Frame(my_canvas2)

   y_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas2.yview)
   y_scrollbar.pack(side=RIGHT, fill=Y)

   y_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
   y_scrollbar.pack(side=RIGHT, fill=Y)

   my_canvas.bind("<Configure>",lambda e: my_canvas.config(scrollregion= my_canvas.bbox(ALL))) 
   my_canvas2.bind("<Configure>",lambda e: my_canvas2.config(scrollregion= my_canvas2.bbox(ALL))) 

   my_canvas.create_window((0,0),window= frame1, anchor="nw")
   my_canvas2.create_window((0,0),window= frame2, anchor="ne")

   with open('master.csv','r') as f:
       reader=csv.reader(f)
       for row in reader:
           if not row==[] and not row[0]=='Admno' and not '' in row:
              for j in range(len(l[1])):
                   if l[1][j][0]==int(row[0]):
                       x=list(l[1][j])
                       x.insert(1,row[1])
                       x.reverse()
                       x=tuple(x)
                       l[1][j]=x
              for j in range(len(l[2])):
                   if l[2][j][0]==int(row[0]):
                       x=list(l[2][j])
                       x.insert(1,row[1])
                       x.reverse()
                       x=tuple(x)
                       l[2][j]=x

   l[1].sort()
   l[1].reverse()
   l[2].sort()
   l[2].reverse()

   risk1=[0.33,0.67,1.0,1.33,1.67]
   risk2=['very low','low','medium','high','very high','severe']

   total=risk2[-1]
   for i in range (len(risk1)):
      if (l[0]/average_transfer_chance)<risk1[i]:
         total=risk2[i]
         break

   if '*' in name:
       total='infected'

   #l[0]*=100
   #l[0]=round(l[0],2)
               
   Label(frame1, text="  Infection Risk: "+total).grid(row=0,sticky=W)

   Label(frame1, text="  Risk posed by:").grid(row=1,column=0,sticky=W,pady=10)

   n1=1

   for i in l[1]:   
           Label(frame1, text=i[1]).grid(row=n1+1, column=0,sticky=W)
           r=risk2[-1]
           for j in range (len(risk1)):
               if (i[0]/average_transfer_chance)<risk1[j]:
                  r=risk2[j]
                  break
           Label(frame1, text=r).grid(row=n1+1, column=1,sticky=W)
           n1+=1

   status='negative'
   if '*' in name:
      status='positive'


   Label(frame2, text="  Infection Status: "+status).grid(row=0,sticky=W)

   Label(frame2, text="  Risk posed  to:").grid(row=1,column=0,sticky=W,pady=10)

   n2=1

   for i in l[2]:   
           Label(frame2, text=i[1]).grid(row=n2+1, column=0,sticky=W)
           r=risk2[-1]
           for j in range (len(risk1)):
               if (i[0]/average_transfer_chance)<risk1[j]:
                  r=risk2[j]
                  break
           Label(frame2, text=r).grid(row=n2+1, column=1,sticky=W)
           n2+=1

   Button(frame1, text='Update contacts', command=update).grid(row=n1+1,column=0,pady=15)

   Button(frame2, text="Change Infection Status", command=toggle).grid(row=n2+1,column=0,pady=15,padx=5)

if c==0:
   create()
   c+=1
