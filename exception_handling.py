x=int(input("enter the number"))

try:
  if (x>10):
   print("x is greater than 10")
  else:
    print("x is less than 10")
except Exception as e:
  print(f"hey you have error{e}")