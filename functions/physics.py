def main():
  energy = formula(int(input("What is the mass in kilograms? ")))
  print(f"energy in joules: {energy}")

def formula(m):
  c = 299792458  #Speed of light m/s
  e = m*c**2  #Formula
  return e

main()