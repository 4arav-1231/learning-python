"""Write a python code for a Castco Store! Where you buy 4 Pizzas for $20 each, 5 Burgers for $25 each, 5 Coke for $10 each and 10 Packets of Chips for $5 each. Calculate and print the final amount.
Apply a discount of 34% and then include 18% tax on the amount after discount and on top of that apply handling charge of $15"""

pizza=4*20
burgers=5*25
coke=5*10
chips=5*10
total = pizza+burgers+coke+chips
print("Your total is:", total)
discount=34
discount_amount=(total*discount)/100
subtotal=total-discount_amount
print("Your discount is:", discount,"% off")
tax=18
tax_amount=(subtotal*18)/100
print("Tax charges are:", tax,"%")
handling_charge=15
print("Handling charge is:", handling_charge)
final_amount=subtotal+tax_amount+handling_charge
print("Final amount is:", final_amount)


