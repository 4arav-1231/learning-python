num=int(input("Choose a number: "))

def numFactorial():
  prod=1
  for i in range(1, num+1, 1):
    prod = prod * i
  return prod


print(f"factorial of {num} is {numFactorial()}.")
