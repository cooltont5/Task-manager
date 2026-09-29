
def start():
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Mark complete")
    print("5.Exit")

def Add(task): 
     tasks.insert(position,task)
     file = open("tasks.txt","w" )
     for task in tasks:
          file.write(task + "\n") 
     file.close


def Remove():
     tasks.pop(location)

tasks = []
position = 0 
num = 0
location = 1
while True:
     start()
     choice = input("What would you like to do? ")
     if choice == "1":
      file = open("tasks.txt")
      for i in tasks:
           print(location,".",i)
           location = location + 1 
      file.close
     if choice == "2":
            task = input("What task would you like to add? ")
            position = position + 1 
            num = num + 1              
            Add(task)
     if choice == "3":
          location = int(input("What task would you like to remove? "))
          if location <= 0 or location > len(tasks):
               print("Please enter a valid number")
          Remove()

          