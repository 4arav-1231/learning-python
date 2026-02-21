# https://cs50.harvard.edu/python/psets/1/meal/

def timecheck():
  time = input("What time is it? ")
  timesplit = time.split(":")
  if int(timesplit[0])>23 or int(timesplit[1])>59:
    return ""
  simpletime = int(timesplit[0])+(int(timesplit[1])/60)
  if simpletime >= 7 and simpletime <= 8:
    return "Breakfast time"
  elif simpletime >= 12 and simpletime <= 13:
    return "Lunch time"
  elif simpletime >= 18 and simpletime <= 19:
    return "Dinner time"
  else:
    return ""
  
print(timecheck())