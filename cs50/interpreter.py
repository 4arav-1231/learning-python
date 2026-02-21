# https://cs50.harvard.edu/python/psets/1/interpreter/

def calculate():
  expression = input("Expression: ")
  expressionSplit = expression.split(" ")
  
  firstValue = expressionSplit[0]
  firstValue = int(firstValue)
  
  lastValue = expressionSplit[2]
  lastValue = int(lastValue)
  
  operation = expressionSplit[1]

  if operation == "+":
    sum = firstValue + lastValue
    return sum
  elif operation == "-":
    difference = firstValue - lastValue
    return difference
  elif operation == "*":
    product = firstValue * lastValue
    return product
  elif operation == "/":
    quotient = firstValue / lastValue
    return quotient

print(calculate())
  