"""Write a python code to input a number and print its factorial"""

num=int(input("Choose a number: "))
prod=1


for i in range(1, num+1, 1):
  prod=prod*i
  print(prod)

print(prod)
