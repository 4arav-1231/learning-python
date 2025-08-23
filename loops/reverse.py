# write a code to input from the user for start and the stop limit and print all the numbers but in reverse order

start=int(input("Choose a start number: "))
stop=int(input("Choose a stop number: "))
for i in range(stop,start-1,-1):
  print(i)