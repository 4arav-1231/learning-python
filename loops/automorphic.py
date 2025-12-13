num = input("choose a number, we will check if it is an automorphic number: ")
numlength = len(num)
num = int(num)
sqrnum=num**2

lstdgt = sqrnum % (10**numlength)
if lstdgt == num:
    print(num, "is an automorphic number\nThe square of", num, "is", sqrnum)
else:
    print(num,"is not an automorphic number\nThe square of", num, "is", sqrnum)



"""25
square = 25
25%10=5

10**length

100
1000
100000
"""