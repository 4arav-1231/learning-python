"""finding a palindrome word"""
def checkWord(word):
  reverse = word[::-1]
  if reverse == word:
    return "is a palindrome"
  else:
    return "is not a palindrome"

word = input("choose a word: ")
result=checkWord(word)
print(word, result)

# test = "javascript"
# print(test[0:4]) 
