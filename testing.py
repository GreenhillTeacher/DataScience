import csv
import math
file = open('insurance.csv')

type(file)
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
age=28
sex=0
bmi= 26.2
num=3
smoker=0
insurance_cost=250*age - 128*sex  + 370*bmi + 425*num+ 24000*smoker - 12500
print(insurance_cost)
rows = []
for row in csvreader:
    rows.append(row)
   
print(rows)
file.close()






 #print(row)
    #print(row[0])
#     if row[1]=="female":
#         row[1]=0
#     else:
#         row[1]=1
    
#     if row[4]=="yes":
#         row[4]= 1
#     else:
#         row[4]=0
    
#     insurance_cost=250*int(row[0])+128*int(row[1])*(-1) + 370*float(row[2])+425*int(row[3])+24000*int(row[4])-12500
#     print("Insurance cost = %.2f \n " % insurance_cost)