def box (word):
  l = len(word)
  print("#"*(l+2))
  print("#"+word+"#")
  print("#" *(1+4))

def low(word):
  print(word.lower())

def up(word):
  print(word.upper())

def repeat(word):
  n = int(input("Number of times to repeat: "))
  for times in range(n):
    if times % 2 == 0 :
      up(word)
    else:
      low(word)

repeat("CocoJambo")

def run():
  w = input("Enter a word")
  opt = int(input())
  print("Choose an option : 1-box\n2-lower\n3-Upper\n4-Mirror\n5-Repetition")
  option =int(input())
  if opt == 1:
    box(w)
  elif opt == 2:
    low(w)
  elif opt == 3:
    upper(w)
  elif opt == 4:
    mirror(w)
  elif opt == 5:
    repeat(w)
  else :
    print("No such option")

run()