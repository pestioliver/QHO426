salary = float(input("enter salary; "))
years = int(input("enter number of years: "))

if years > 2 :
  if salary < 25000:
    salary = salary * 1.1
    print(f"your new salary will be {salary}")

  else: 
    salary = salary + 100
    print(f"small change , you will now earn £{salary}")
elif years > 1:
  print("no salary increase for you , sorry")

else : 
  if salary < 15000 : 
    print("oops your salary should be £20000")
    salary = 20000

print("let us for work  the good of the company")