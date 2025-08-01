"""Write a program to input the number of hours a car is parked and display the total amount, if the fee is 
$5 per hour for first 2 hrs
$4 per hour for next 5 hours
$3 for rest
"""

hrs=float(input("How many hrs have you parked your car: "))

if hrs > 7:
  slabss = hrs - 7
  slabsss = slabss *3
  print("Your cost for parking is",slabsss + 30)
else:
  slab = hrs*5
  slabs = hrs -2
  print("Your cost for parking is",slab - slabs)
