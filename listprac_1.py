# # #list can print different types like strings,integers,floats etc.....,,
# # #lists are ordered # can print duplicate values 
# # #lists is donated by [] whereas tuple is doneted by ()
# colors= ["Red","Blue","Red","Black",22]
# cars = ["BUGATI","LAMBORGINI","AUDI","BENZ"]
# numbers = [1,4,6,2,10]

# cars.sort()
# numbers.sort(reverse=True)
# print(numbers)
# print(cars)
#newList = [x.lower() for x in cars]
#print(newList)
#     expression item list condition
# #[print(x) for x in cars]
# newlist = []
# #if a is in the car , add that to new list
# for i in cars:
#     if "A" in i:
#         newlist.append(i)
#     print(newlist)   
# #for x in range(len(cars)):
#  #   print(cars[x])


# # Players = ("Dhoni","Ronaldo","Virat")

# # colors[0:2] = ["Yellow","Orange"]
# # # colors[2] = "Green"
# # #print(colors[1:4])
# # #Insert will add a specified at a certain position in the list
# # #colors.insert(2,"Indigo")
# # #append will add the element at last
# # #colors.append("BUGATI")

# # #colors.extend(cars)
# # #"remove" removes a specific element
# # #colors.removes("Red")
# # #"tuple objects does not support item assigment"
# # #pop removes from a specific index
# # # colors.pop(1)

# # #del colors[0]
# # colors.clear()
# # print(colors)  




numbers = [1,2,3,4,5]
null=[]
#write a program to turn every item of list into its square

#output   [1,4,9,16,25]

for i in numbers:
    i = i**2
    null.append(i)
print(null)
