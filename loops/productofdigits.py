# Write a Program to input a number and print the product of digits.

# Example : 253
# Output : 2*5*3
#           = 30

num = int(input("chose a num: "))
product = 1

while (num > 0):
  digit = num%10
  product = product * digit
  num = num//10

print("the product of your digits is ", product)