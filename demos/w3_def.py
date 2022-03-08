# def function = specifying what it is and what it does
#parameter = data given into the function
def calc_area(h=8,b=1):
  
  area = 0.5*h*b
  print(f"The area is {area} cm^2")
#call to the function to make it run
calc_area(2,10)
calc_area(9)
calc_area()
calc_area(b=10)#h default is 8 because we have not changed in the brackets
print(f"The area is {calc_area(80,20)} cm^2")