my_list=["adil",1,2,3,4,5,0.1]
print(my_list)

my_list.append("Banana") #used to add something to list
print(my_list)

my_list.pop() #used to delete something from list
print(my_list)

for i in reversed(my_list): #used to iterate in revsersed order
  print(i)

#list comprehension

list=[1,2,3,4,5,6,7,] #taking square of each element in a list array and store in new list array
new_list=[i*i for i in list]
print(new_list)

#for i in list:
 # new_list.append(i*i)

#print(new_list)