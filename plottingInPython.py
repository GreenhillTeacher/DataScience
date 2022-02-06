#Maria Suarez
#Exercices
#Learning Numpy
import numpy as np
import csv, matplotlib.pyplot as plt
file = open('insurance.csv')
type(file)
csvreader = csv.reader(file)
header = next(csvreader)
newData = []
for row in csvreader:
    if row[1]=="female":
        row[1]=int(0)
    else:
        row[1]=int(1)
    
    if row[4]=="yes":
        row[4]= int(1)
    else:
        row[4]=int(0)
   
    newData.append(row)
file.close()
#print(newData)
#arr = numpy.array(lst)
dataSample=np.array(newData)
#print(dataSample[0][2])  x[:,1].astype(int)
xData=dataSample[:,0].astype(int)
yData=dataSample[:,2].astype(float)
#plt.figure()
plt.scatter(xData,yData)
plt.show() 
