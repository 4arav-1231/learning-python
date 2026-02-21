#https://cs50.harvard.edu/python/psets/2/camel/

def check(camel_case):
  current_txt = ""
  for i in range(len(camel_case)):
    if camel_case[i].isupper():
      current_txt = current_txt + "_" + camel_case[i].lower()
    else:
      current_txt = current_txt + camel_case[i]
  return current_txt

camel_case = input("camel case: ")

print("snake case:", check(camel_case))