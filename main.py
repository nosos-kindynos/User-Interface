import os
from inp import admno
import csv

l=[]

with open ('master.csv','r') as f:
              reader=csv.reader(f)
              for row in reader:
                  if not row ==[] and row[0]==admno:
                      l=row
                      break
                      print(l)
                      #print(l)
                    
if len(l)==2 or l[2]=='':
    import trialregister
    
else:
    import login
