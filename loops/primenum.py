# Write a python code to input a number and check if it is prime number or not

while True:
  num = int(input("\nchoose a number: "))

  amt = 0

  for i in range(1, num+1, 1):
    numcheck = num%i
    if numcheck == 0:
      amt+=1

  if amt == 2:
    print(num, "is prime!")
  elif amt<2:
    print(num, "is not prime nor composite!")
  else:
    print(num, "is composite!")