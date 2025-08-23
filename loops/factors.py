num=int(input("Choose a number: "))



for i in range(1,num+1):
  numcheck = num%i
  if numcheck == 0:
    print(i)
    
