# Student Grade Calculator

name = input("Enter Student Name: ")
m1 = int(input("Enter Marks 1: "))
m2 = int(input("Enter Marks 2: "))
m3 = int(input("Enter Marks 3: "))
total = m1 + m2 + m3
avg = total / 3
if avg >= 90:
    grade = "A"
elif avg >= 75:
    grade = "B"
elif avg >= 60:
    grade = "C"
elif avg >= 35:
    grade = "D"
else:
    grade = "F"

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average:", avg)
print("Grade:", grade)