def convert(input):
  a= input.replace(":)","🙂")
  b= a.replace(":(","🙁")
  return b

def main():
  string = input("write anything: \n")
  print()
  print(convert(string))

main()
      


# a="harsh@gmail.com@"
# result=a.replace("@","#")