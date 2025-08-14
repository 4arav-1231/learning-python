import random

while True:
  print("\nPlay rock paper scissors, Choose \n1 for rock\n2 for paper\n3 for scissors\n-1 to exit")
  Humanchoice=int(input("Choose rock, paper, or scissors: "))

  if  Humanchoice == -1:
    break
    
  AIchoice=random.randint(1,3)
  print("AI chose: ", AIchoice)

  if (Humanchoice ==1 and AIchoice==2)or (Humanchoice == 2 and AIchoice == 3) or (Humanchoice == 3 and AIchoice == 1):
    print("AI won!")
    
  elif (Humanchoice ==2 and AIchoice==1)or (Humanchoice == 3 and AIchoice == 1) or (Humanchoice == 1 and AIchoice == 3):
    print("Human won!")
    
  elif Humanchoice == AIchoice:
    print("It's a tie!")
    
  elif Humanchoice>3:
    print("WR0NG INPUT")
  