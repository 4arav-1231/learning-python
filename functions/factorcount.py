#write a function that takes the number as parameter and returns how many factors it has.

"""
def factorcount(num):
    counter = 0

    for factor in range(1,int(num/2)+1):
    if num%factor == 0:
      counter = counter+1

    return counter
    
num = int(input("choose a number: "))
print(factorcount(num))
"""

def factorcount(num):
  factors = []
  for factor in range(1,int(num/2)+1):
    if num%factor == 0:
      factors.append(factor)

  return factors

num = int(input("choose a number: "))
print(factorcount(num))