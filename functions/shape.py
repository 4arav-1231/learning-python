def areaCheck(sidelength=10):
  area = sidelength**2
  return area

side = int(input("Enter side length for a square: "))
print(f"area is {areaCheck(side)}")