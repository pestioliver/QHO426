def shop():
  items = {"fish": 1,"eggs": 1.99,"oil": 4.99,"bread": 2 ,"milk": 1.69, "chocolate":0.99, "salad":0.99}
  return items

def view_all(product = {}):
  for i,j in product.items():
    print(f"{i}-----£{j}")

def basket():
  b = []
  while True:
    item = input("Enter next item or \"to stop: ")
    if item.lower() == "stop":
      break
    else:
        q = int(input(f"Enter quantity of {item}: "))
        for i in range(q):
          b.append(item.lowe())
  return b

def till(basket = []):
  all_items = shop()
  total = 0.0
  for product in basket:
      total += all_items[product]
  return total
def run():
  print("welcome to Pete`s shop - the best one ever! please have a look")
  view_all(shop())
  b = basket()
  while True:
    print("Are you ready to pay?: ")
    response = input()
    if response.lower() == "yes":
      to_pay = till(b)
      print(f"Pay £{to_pay} or i will call the cops!")
      break
    else : 
      b2 = basket()
      b += b2

run()