#https://cs50.harvard.edu/python/psets/2/coke/
amount_due = 50

while amount_due > 0:
  money_paid = int(input("Money paid: "))
  if money_paid != 25 and money_paid != 10 and money_paid != 5:
    print("Invalid money")
  amount_due = amount_due-money_paid
  if amount_due <= 0:
    print(f"Change owed: {amount_due*-1}")
  else: 
    print(f"Amount due: {amount_due}")
  print()