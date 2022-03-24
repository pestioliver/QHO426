def interests():
  print("Enter your interest, one after the other,and enter\"stop\"When you are done")
  s1 = set()
  while True:
    interest = input()
    if interest.lower() == "stop":
      break
    else:
      s1.add(interest)
  return s1

def tinderDaSecond():
  print("First person: ")
  p1 = interests()
  print("Second person: ")
  p2 = interests()
  common = p1.intersection(p2)
  if len(common) >= 3:
    print(f"Yay you are amatch made in heaven {len(common)} common interest")
  else:
    print(f"Well, i dont think it would work your only have {len(common)}common interest :( ")

tinderDaSecond()
  
  
  