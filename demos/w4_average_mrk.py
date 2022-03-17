def generate():
  name = input("Enter name: ")
  mrk = int(input("Enter final mark: "))
  return name , mrk

def list_student(n):
  lista = list()
  for i in range(n):
    lista.append(generate())

  return lista

def average_mrk(lista = []):
  total = 0
  for tup in lista:
    total += tup[1]
  aver = total/len(lista)
  return aver

def run():
  lista = []
  while True:
    opt = int(input("Menu:\n1-Populate list of students\n2-Calculate average mark\n3-Change mark of a student\n9-Exit\n"))
  

    if opt ==1:
      n = int(input("Enter number of students: "))
      lista = list_student(n)
    elif opt == 2 :
      print(f"Average mark is : {average_mrk(lista)}")
    elif opt == 3 :
      name = input("Enter the name of student: ")
      for i in lista:
        if i[0].lower() == name.lower():
          n_mrk = int(input("Enter new mark : "))
          lista.remove(i)
          lista.append((name,n_mrk))
  
    elif opt == 9:
      break
          
  
run()