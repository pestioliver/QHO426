name = input("enter your name: ")

#len() - function that return the lenght of string

if len(name) > 9:
  print("your name is too long to remember. Can i use a nickname please?")
  print("this prints too!")
elif len(name) <= 3 :
  print("that is very short  - easy to remember")
elif name == "Martha":
  print("Why did you say that name")
else:
  print("oh your name is pretty short")

print("nice to meet you anyway, {}".format(name))