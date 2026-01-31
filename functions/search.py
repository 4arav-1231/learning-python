"""Write a python function that takes numbers using arbitary argument and take a number to search and print result for the search"""
def search(searchnum,*storenum):
  if searchnum in storenum:
    print(f"{searchnum} is in {storenum}")
  else:
    print(f"{searchnum} is not in {storenum}")

search(5, 6, 7, 3, 1, 5, 3, 2)