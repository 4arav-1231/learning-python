"""Aarav goes to a walmart store to buy some toys, he bought 1 set of skates for $40, 4 set of Avengers character for $10 each, a helmet for $50 and 5 Barbie Sets (to gift sisters) for $30 each. 
If he was allowed a discount of 20%, Write a python code to print the final amount"""


skates=40
avengers=4*10
helmet=50
barbie=5*30
total = skates+avengers+helmet+barbie
discount=20
disc_amt=(total*discount)/100
subtotal=total-disc_amt

print("Your total was: ", total)
print("Your discount is: ", discount, "%")
print("Your subtotal is: ",subtotal)
