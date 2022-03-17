def adding(lista = []):
    n_member = input("Enter new avenger: ")
    lista.append(n_member)
    return lista

def removing(lista = []):
    rejected = input("Enter avenger to be removed: ")
    if rejected in lista:
        lista.remove(rejected)
    return lista

def printing(lista =[]):
    for hero in lista:
        print(f"The mighty {hero} is part of Avengers!")

def run():
    avengers = []
    while True:
        opt = int(input("Avengers, Assemble!\n\n1-Add a new avenger\n2-Remove an avenger\n3-Check on the team\n9-Exit\n"))
        if opt == 1:
            avengers = adding(avengers)
        elif opt == 2:
            avengers = removing(avengers)
        elif opt == 3:
            printing(avengers)
        elif opt == 9:
            break
        else:
            print("No such option available! Try again!")

run()
        