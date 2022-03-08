while True:
    print("Please choose one of the following options:\n\n1-Nice Message\n2-Area of Rectangle\n3-Area of Triangle\n4-Times Table\n0-Exit")
    opt = int(input())
    
    if opt == 1:
        print("You do not smell too bad today!")
    elif opt == 2:
        w = float(input("Enter width: "))
        h = float(input("Enter height: "))
        area = w*h
        print("The area is {}".format(area))
    elif opt == 3:
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        area = 0.5*b*h
        print("The area is {}".format(area))
    elif opt == 4:
        n = int(input("Enter whole number: "))
        for i in range(1,11):
            print(f"{i}x{n} = {i*n}")
        print("That's all folks!")
    elif opt == 0:
        break
    else:
        print("Whoooopsie! - no such option, my frined!")