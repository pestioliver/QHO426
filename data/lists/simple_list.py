def directions():
  directions = list()
  directions.append("Move forward")
  directions.append("Move backward")
  directions.append("Turn left")
  directions.append("Turn right")
  #directions = ["Move forward","Move backward","Turn left","Turn right"]
  return directions

def run():
  print(directions())

run()