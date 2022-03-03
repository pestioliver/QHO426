age = int(input("enter age: "))
ch = int(input("enter number of children: "))

if age > 25 and ch > 0:
  print("you are a young parent")
  print(f"next year you will be {age+1} years old ")

elif age > 55 and ch >= 0:
  print("your children will support you in old age")

elif age < 18 or ch==0:
  print("There is still time to have a child , if you want")

else:
  print("You are not so young")
  print("we are going to live a long life anyway")