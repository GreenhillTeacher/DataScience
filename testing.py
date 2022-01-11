import csv
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
    print(row)
    print(row[0])
#print(rows)
file.close()