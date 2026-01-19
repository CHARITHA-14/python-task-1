# Take marks input from user
marks = int(input("Enter your marks (0-100): "))

# Check for invalid marks
if marks < 0 or marks > 100:
    print("Invalid marks! Please enter marks between 0 and 100.")

# Determine grade
elif marks >= 90 and marks <= 100:
    print("Grade: A")
    if marks >= 95:   # Nested condition
        print("Outstanding distinction!")
    else:
        print("Excellent performance!")

elif marks >= 75 and marks < 90:
    print("Grade: B")
    print("Very good job!")

elif marks >= 60 and marks < 75:
    print("Grade: C")
    print("Good effort!")

elif marks >= 40 and marks < 60:
    print("Grade: D")
    print("Needs improvement.")

else:
    print("Grade: F")
    print("Fail. Better luck next time.")
