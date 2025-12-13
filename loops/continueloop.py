limit = int(input("choose a limit: "))
num=int(input("which number do you want to skip: "))

for i in range(0,limit):
  if i == num:
    continue
  print(i)