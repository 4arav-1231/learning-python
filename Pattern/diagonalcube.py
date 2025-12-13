"""

/****
*/***
**/**
***/*
****/ 
"""
rows = int(input("how many rows you want?: "))
cols = int(input("how many columns you want?: "))

for i in range(rows):
  for j in range(cols):
    if i == j:
      print("/", end=" ")
    else:
      print("*", end=" ")
  print()