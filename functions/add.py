#basic function
"""
def addnum():
  a = int(input("pick a number: "))
  b = int(input("pick another number: "))
  c = a+b
  print(c)

addnum()
"""
#parameters
"""
def addnum(x,y):
  c = x+y
  print(c)

a = int(input("pick a number: "))
b = int(input("pick another number: "))

addnum(a,b)
"""
#return

def addnum(a,b):
  c = a+b
  return c

a = int(input("pick a number: "))
b = int(input("pick another number: "))

result = addnum(a,b)

print(result)
