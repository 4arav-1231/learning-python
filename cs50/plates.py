from curses.ascii import isalpha

plate = input("Plate: ")
def is_valid():
  if len_check() and letter_check() and number_check() and punctuation_check():
    return True
  else:
    return False

def len_check():
  if len(plate) > 1 and len(plate) < 7:
    return True
  else:
    return False

def letter_check():
  if not (plate[0].isalpha()):
    return False
  if not (plate[1].isalpha()):
    return False
  return True


def number_check():
  for i in range(len(plate)):
    if plate[i].isnumeric():
      if plate[i] == "0":
        return False
      stringg = plate.split(plate[i])
      return stringg[1].isnumeric()

def punctuation_check():
  return plate.isalnum()

if is_valid():
  print("Valid")
elif not is_valid():
  print("Invalid")