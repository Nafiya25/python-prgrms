# Write a program to determine the grade based on marks.

# Criteria:
# Marks >= 90: A
# Marks >= 80: B
# Marks >= 70: C
# Marks >= 60: D
# Else: F
# python
# Copy code
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")

