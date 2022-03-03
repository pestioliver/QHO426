print("Please enter the first number : ")
n1 = int(input())
print("Please enter the second number : ")
n2 = int(input())
odd = 0 
even = 0
if n1 % 2 == 0:
  even += 1

else:
  odd +=1

if n2 % 2 == 0:
  even += 1

else:
  odd += 1

print("There were so many even number ({}) and so many odd({}) numbers".format(even,odd))