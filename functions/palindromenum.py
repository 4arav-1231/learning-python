"""finding a palindrome num"""
def palindromeCheck(num):
  storednum = num
  counter=0
  while num>0:
    digit = num%10
    counter = counter*10+digit
    num = num//10
    
  if counter == storednum:
    return "a palindrome!"
  else:
    return "not a palindrome!"

num = int(input("choose a number we will check if its a palindrome: "))
result = palindromeCheck(num)
print(num, "is", result)