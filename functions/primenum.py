"""Check if number is prime using functions"""

def primeCheck(num):
  check = 0
  for i in range(2, num//2+1):
    if num%i == 0:
      check = check+1
  if check > 0:
    return "composite"
  else:
    return "prime"

num = int(input("choose a number right now: "))
print(num, "is", primeCheck(num))