import csv
def reading_csv():
  with open ("students.csv") as students:
    csv_reader = csv.reader(students)
    next(csv_reader)
    total = 0
    count = 0
    for row in csv_reader:
        print(row)
        total += int(row[2])
        count += 1

  print(f"The average mark of exam 1 was {total/4}")

def writing_csv():
  with open("students.csv","a") as s:
    csv_writer = csv.writer(s)
    while True:
      name = input("Enter name: ")
      id = input("Enter ID: ")
      e1 = int(input("Enter Exam 1 : "))
      e2 = int(input("Enter Exam 2 : "))
      csv_writer.writerow([name,id,e1,e2])
      if input("Shall we stop? (type Y or N): ").upper() == "Y":
        break
    
reading_csv()
writing_csv()
reading_csv()