def perfectCheck(num):
  prod = 1
  for factor in range(1,int(num/2)+1):
    if num%factor == 0:
      prod = prod * factor
  if num == prod:
    return f"{num} is a perfect number"
  else:
    return f"{num} is not a perfect number"

num = int(input("choose a number: "))
print(perfectCheck(num))