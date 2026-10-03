from pathlib import Path

def start():
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Mark complete")
    print("5.Exit")

def Add(task): 
     tasks.append(task)
     save()

def Remove(location):
     location = location - 1
     tasks.pop(location)
     save()

def check():
     show()
     location = input("What task would you like to remove? ")
     if location.isdigit():
          location = int(location)
          if location <= 0 or location > len(tasks):
               print("Please enter a valid number")
               check()
          else:
               Remove(location)
     else:
          print("Please enter a number")
          check()

def check_1():
     show()
     location_1 = input("What task would you like to mark as complete ? ")
     if location_1.isdigit():
          location_1 = int(location_1) 
          if location_1 <= 0 or location_1 > len(tasks):
               print("Please enter a valid number")
               check_1()
          else:
               complete(location_1)
     else:
          print("Please enter a number")
          check_1()          

def complete(location_1):
     location_1 = location_1 - 1
     completed_task = tasks[location_1]
     if "completed" in completed_task:
          print("This task is already marked as complete")
     else:
          completed_task = completed_task + " completed"
          tasks[location_1] = completed_task
          save()
        
def load():
     file =  open(file_path,"r")
     for line in file:
          if line.strip():
               tasks.append(line.strip())
     file.close()

def show():
     for location,task in enumerate(tasks,1):
          print(location,".",task)

def save():
     file = open(file_path,"w" )
     for task in tasks:
          file.write(task + "\n") 
     file.close()


file_path = Path(__file__).parent/"tasks.txt"
tasks = []
running = True 

load()
while running:
     start()
     choice = input("What would you like to do? ")
     if choice == "1":
          show()
     if choice == "2":
            task = input("What task would you like to add? ")           
            Add(task)
     if choice == "3":
           check()
     if choice == "4":
          check_1()
     if choice == "5":
          running = False
          