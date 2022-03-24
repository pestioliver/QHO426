#initialise empty dictionary
phonebook = {}
d2 = dict()
#Initialise non-empty dictionary
piotr = {"Name":"Piotr","Age":18, "Doggo":False, "Title":"Mr"}
#printing full dictionary
print(piotr)
print(len(piotr))
#Acess invididual elements from the dictionary
print(piotr["Age"])
print(piotr["Doggo"])
print(f'{piotr["Name"]} is {piotr["Age"]}years old and their title is {piotr["Title"]}')
#add elements to dictionary
phonebook["Hugo"] = "+4477019191"
phonebook["Sadia"]= "+4477231313"
phonebook["Lucian"] = "+4421312311"
phonebook["Roxana"] = None
print(phonebook)
#add more items to the phonebook
for i in range(3):
  name = input("Enter new name : ")
  numb = input(f"Enter number for {name}: ")
  phonebook[name] = numb
print(phonebook)
#Calling a particular person from phonebook!
name = input("Who you gonna call: ")
if name in phonebook:
  print(f"Calling {name} with number {phonebook[name]}")
else:
  print(f"This person is not in your phonebook!")