#declare an empty list 
bleh = []
meh = list()
#declare a non-empty list
yummy = ["pizza","lasagne","fish and chips"]
#print the entire list
print(yummy)
#printing a single item
print(yummy[2])
#print some items
print(yummy[:2])
#add elements to our list-at the end
print (bleh)
bleh.append ("sea food")
bleh.append ("soup")
bleh.append ("liver")
print(bleh)
#adding multiple items to the list , based on user input
for i in range(5):
  yummy.append(input("Enter yummy food: "))#user add items to the list
print (yummy)
#add new items to the list at specific position
bleh.insert(1,"mashed potatoes")
bleh.insert(3,"cabbage")
print(bleh)
#remove items from list based on names
if "potatoes" in bleh:
  bleh.remove("potatoes")
bleh.remove("soup")
print (bleh)
#remove items by index
bleh.pop(1)
print(bleh)
#remove item by index other way
del bleh[1]
print(bleh)
#extend a list
bleh.extend(["fish,frankfurters,beetroot"])
print(bleh)
bleh.extend(yummy)
print(bleh)
#checking for particular data type
lista = ["fred",True,6,8,-3,6,False,"lala",55]
for item in lista:
  if isinstance(item,int):
    print(item)