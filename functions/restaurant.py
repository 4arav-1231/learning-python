"""
Resturant Menu Manager:

Project Description: Create a resturant manager application that allows users to add item name, view the items, search for specific item, and delete item.
Key Features: Add item, View item, Search item, Delete item.
"""
"NOTE TO SELF"
"use a list"

menu = []
def addItem(item):
  menu.append(item)

def viewItem():
  if not menu:
    print("Menu is empty.")
  for i in menu:
    print(i)

def searchItem(item):
  if item in menu:
    print(f"{item} is on menu.")
  else:
    print(f"{item} is not on menu")

def deleteItem(item):
  if item in menu:
    menu.remove(item)
  else:
    print(f"{item} is not on menu")
    
while True:
  choice = input("Enter 1 to add food, 2 to view menu, 3 for searching food, 4 for deleting food, 5 to exit: ")

  if choice == "1":
    item = input("Enter a food: ")
    addItem(item)
  elif choice == "2":
    viewItem()
  elif choice == "3":
    item = input("Enter a food: ")
    searchItem(item)
  elif choice == "4":
    item = input("Enter a food: ")
    deleteItem(item)
  elif choice == "5":
    break
  

  


