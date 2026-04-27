my_list=[1,2,3,4,5,6,7,8]

def square(x):
  return x*x


result=list(map(square,my_list))

print(result)



my_arr=[1,2,3,4,5,6,7,8]

def square(x):
  if (x%2==0): 
   return x*x


result=list(filter(square,my_arr))

print(result)


