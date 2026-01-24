def numAutomorphic(num):
    numlength = len(num)
    num = int(num)
    sqrnum=num**2

    lstdgt = sqrnum % (10**numlength)
    if lstdgt == num:
        return f"{num} is an automorphic number\nThe square of {num} is {sqrnum}"
    else:
        return f"{num} is not an automorphic number\nThe square of {num} is {sqrnum}"
        
num = input("choose a number, we will check if it is an automorphic number: ")

print(numAutomorphic(num))