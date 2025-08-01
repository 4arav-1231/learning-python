# write a code to input year of birth and print age
import math
birthyr = int(input("What year were you born: "))
months = int(input("Which month were you born in: "))
currentyr=2025
currentmnt=8
age = math.floor((currentyr+(currentmnt/12))-(birthyr+(months/12)))
print("You are",age,"years old!")
