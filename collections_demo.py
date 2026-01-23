# List (mutable)
students = ["Anu", "Ravi", "Anu", "Kiran"]

# Add elements
students.append("Sita")

# Remove element
students.remove("Ravi")

# Sort list
students.sort()

print("Student List:", students)


# Tuple (immutable – fixed data)
college_info = ("ABC College", "CSE", 2026)
print("College Info:", college_info)


# Convert list to set (remove duplicates)
student_set = set(students)
print("Unique Students:", student_set)


# Another set
new_students = {"Kiran", "Manoj", "Sita"}

# Set operations
print("Union:", student_set | new_students)
print("Intersection:", student_set & new_students)
print("Difference:", student_set - new_students)


# Iteration over collections
print("\nIterating List:")
for s in students:
    print(s)

print("\nIterating Tuple:")
for info in college_info:
    print(info)

print("\nIterating Set:")
for s in student_set:
    print(s)


# Mutable vs Immutable comparison
students[0] = "Charitha"      # Allowed (list is mutable)
# college_info[0] = "XYZ"     # Not allowed (tuple is immutable)

print("\nAfter modification:")
print("Students:", students)
print("College Info:", college_info)
