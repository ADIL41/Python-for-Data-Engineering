my_student=['Name',"roll no","class","semester","section","institete"]
for i in my_student:
  print(i)

for i in range(1,11):
  print(i)


table=["order","products","catagory"]

for i in table:
  if(i.lower()=="order"):
    print(i)


shop_items = ["Apples", "Bananas", "Milk", "Bread", "Coffee"]

for a in shop_items:
  
  if (a.lower()=="bread"):
    continue   #bread is skip only 
  print(a)
  
x=1
while(x<12):  #while loop is used to brak statement mostly
  print(x)
  x=x+1
