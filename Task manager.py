
from pathlib import Path


def start():
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Mark complete")
    print("5.Exit")

def Add(task): 
     tasks.append(task)
     file = open(file_path,"w" )
     for task in tasks:
          file.write(task + "\n") 
     file.close()


def Remove(location):
     location = location - 1
     tasks.pop(location)
     file = open(file_path,"w" )
     for task in tasks:
          file.write(task + "\n") 
     file.close()

def check():
     location = int(input("What task would you like to remove? "))
     if location <= 0 or location > len(tasks):
          print("Please enter a valid number")
          check()
     else:
          Remove(location)

file_path = Path(__file__).parent/"tasks.txt"
tasks = []
location = 0
validity = True

while True:
     start()
     choice = input("What would you like to do? ")
     if choice == "1":
      for location,task in enumerate(tasks,1):
           print(location,".",task)
     if choice == "2":
            task = input("What task would you like to add? ")           
            Add(task)
     if choice == "3":
           check()
          