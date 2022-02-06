# myList=["apple","banana", "mango", "berries", "papaya"]

# for x in myList:
#     print(x, end='  ')

# print()
# print(myList[2:4])
# print(myList[-3:])
# if "apple" in myList:
#     print ("apple is in the list")

# myList.append("grapes")
# myList.insert(2,"grapes")
# print(len(myList))
# print(myList)
# print(myList.count("grapes"))
# miList2=[]
# myList2= myList.copy()
# print(myList2)
# myTuple=(1,3,4,6,8)
# index1= myList.index("grapes")
# print (index1, end=" index")
# print()
# if 5 not in myTuple: 
#     list1= list(myTuple)
#     list1.insert(3,5)
#     myTuple=tuple(list1)
# print(myTuple)
mySet={"apple","mango", 2, 3, "grapes", "apple"}
# mySet.add("banana")
# print(len(mySet))
# for x in mySet:
#     print(x, end= ' ')
# mySet.update(["cherries","papaya", "orange"])
# for x in mySet:
#     print(x, end= ' ')
# mySet2={ 2,3,4,5}
# print(mySet2)
# mySet3= mySet2.difference(mySet)

# mySet4=mySet.union(mySet2)
# print(mySet4)
# myDict={"name":"Maria", "age":30, "city":"dallas"}
# print("name of student", myDict['name'], end=' ')
# print("age =", myDict['age'], end=' ')
import collections, re
n = int(input("Number of subjects: "))
item_order = collections.OrderedDict()
for i in range(n):
   sub_marks_list = re.split(r'(\d+)$',input("Input Subject name and marks: ").strip())
   subject_name = sub_marks_list[0]
   item_price = int(sub_marks_list[1])
   if subject_name not in item_order:
       item_order[subject_name]=item_price
   else:
       item_order[subject_name]=item_order[subject_name]+item_price
           
for i in item_order:
   print(i+str(item_order[i]))