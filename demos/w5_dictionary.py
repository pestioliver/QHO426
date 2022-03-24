#initialise an empty set
s = set()
s = {}
#Check the data type is "set"
print(type(s))
#Initialise non-empty set
colours = {"blue","purple","yellow","red","green"}
print(colours)
#adding elements to a set
colours.add("Magenta")
colours.add("turquise")
print(colours)
#remove item from set
colours.remove("yellow")
print(colours)
#Uniqueness of items within a set
colours.add("red")
colours.add("purple")
#check membership
if "blue" in colours:
  print("Yes it inside the set")
else:
  print("This colour not inside the set")

c = {"blue","red","rainbow","black","white","cyan","burgundy","biege"}

#Union - joining two set together , not keeping any duplicates
c2 = colours.union(c)
print(c2)
print(colours)
print(c)
#Intersection - looking at "common" elements in both sets
c3 = colours.intersection(c)
print(c3)
#Difference of two sets - keep only elements in one set , not in the other
c4 = colours.difference(c)
c5 = c.difference(colours)
print(c4)
print(c5)