def movement():
  path=["Move forward  ",10,"Move backward ",5,"Turn left" ,3,"Turn right ",1]
  return path

def run():
  print("Moving,,,,")
  lista = movement()
  for i in range(0,8,2):
    print(f"{lista[i]}for{lista[i+1]}steps")

run()