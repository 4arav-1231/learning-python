def areaCheck(le=1, b=2):
  area = le*b
  return area

len = int(input("Enter length of an rectangle: "))
bre = int(input("Enter breadth of an rectangle: "))
print(f"Area of rectangle is {areaCheck(len, bre)}")