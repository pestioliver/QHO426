print("Where should i look?")
answer = input()
if answer == "in the bedroom" : 
  print("where in the bedroom should i look?")
  answer2 = input()
  if answer2 == "under the bed":
    print("Found some,shoes,but no battery")

  else:
    print("Found some mess, but no battery")

elif answer == "in the bathroom":
  print("Where in the bathroom should i look")
  answer2 = input()
  if answer2 == "in the bathtub":
    print("Found rubberduck,but no battery")
  else:
    print("Found a wet surface , but no battery")

elif answer == "in the lab":
  print("Where in the lab should i look?")
  answer2 = input()
  if answer2 == "on the table":
    print("yes i found the battery")

  else: 
    print("Found some tools, but no battery")

else:
  print("i do not know where that is , but i will keep looking")