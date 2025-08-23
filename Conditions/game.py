import random

while True:
  n=int(input("\nChoose a Level above zero(enter 0 to stop): "))
  if n==0:
    print("Game quit")
    break
  if n<1:
    print("Invalid number")
    continue
  rn=random.randint(1,n)

  while True:
    gn=int(input(f"\nGuess the number that we randomly generated.\nThe number is more than 0 and less than {n+1}: "))
    if gn>rn:
      print("\nNumber too large, Try again")
    elif gn<rn:
      print("\nNumber too small, Try again")
    else:
      print("\nYou guessed it right! The answer is: ",rn)
      break