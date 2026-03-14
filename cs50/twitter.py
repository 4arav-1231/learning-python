
def omit_vowels(inpt):
  input_fix=""
  for i in range(len(inpt)):
    if inpt[i]!= "a" and inpt[i]!="e" and inpt[i]!="i" and inpt[i]!="o" and inpt[i]!="u":
      input_fix = input_fix + inpt[i]
  return input_fix
      
inpt = input("Input: ")
print(f"Output: {omit_vowels(inpt)}")
