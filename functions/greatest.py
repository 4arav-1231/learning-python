"""write a program to make a function that takes two words and returns the bigger word"""

def wordCheck(word1, word2):
  wordleni = len(word1)
  wordlenv = len(word2)
  if wordleni > wordlenv:
    return word1
  elif wordlenv > wordleni:
    return word2
  else:
    return "Both words are equal"

wordi = input("Check which words are longer.\nType any word: ")
wordv = input("Type another word: ")
result = wordCheck(wordi,wordv)

print(result)

"""finding a palindrome word"""