# https://cs50.harvard.edu/python/psets/1/extensions/
# file="trip.jpg"
# result=file.split(".")
# print(result)



def fileType():
  file = input("File name: ")
  splitfile = file.split(".")
  filetype = splitfile[1]
  if (filetype == "gif") or (filetype == "jpeg" or filetype == "jpg") or (filetype == "png"):
    return f"image/{filetype}"
  elif (filetype == "pdf") or (filetype == "zip"):
    return f"application/{filetype}"
  elif (filetype == "txt"):
    return "text/plain"
  else:
    return "application/octet-stream"

print(fileType())