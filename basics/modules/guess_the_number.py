import random
minimum = int(input("Please enter minimum value"))
maximum = int(input("Please enter maximum value"))

x = random.randrange(minimum,maximum)
print(f"I am thinking of a number between {minimum} and {maximum}.Can you guess what it is?")


while True:
  guess = int(input("Have a guess: "))
  if guess < x:
    print("Your guess is too low.")

  elif guess > x :
    print("Your guess is too high")
  else:
    break
  print("Try again: ")
print("Congratulation! You guessed ")