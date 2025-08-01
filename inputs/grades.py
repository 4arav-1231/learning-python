"""Write a python code to take input of marks in 5 subjects and print the total and the average."""

math_marks=float(input("Type your marks in math:"))
english_marks=float(input("Type your marks in english:"))
gym_marks=float(input("Type your marks in gym:"))
science_marks=float(input("Type your marks in science:"))
art_marks=float(input("Type your marks in art:"))
total_marks=math_marks+english_marks+gym_marks+science_marks+art_marks
avg_marks=total_marks/5

print("Your total marks are:", total_marks)
print("Your avg marks are:", avg_marks)
if avg_marks>75:
    print("You passed!")
else:
    print("You failed!")


 