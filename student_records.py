import json

# 2. Store student details using dictionary
student = {
    "id": 101,
    "name": "Charitha",
    "age": 20,
    "course": "Computer Science",
    "cgpa": 8.7
}

print("Original Student Dictionary:")
print(student)
print("-" * 40)

# 3. Access keys and values
print("Accessing Keys and Values:")
print("Keys:", student.keys())
print("Values:", student.values())
print("-" * 40)

# 4. Update and delete entries
# Update
student["cgpa"] = 9.0
student["age"] = 21

# Delete
del student["course"]

print("After Update and Delete:")
print(student)
print("-" * 40)

# 5. Loop through dictionary
print("Looping through dictionary:")
for key, value in student.items():
    print(f"{key} : {value}")
print("-" * 40)

# 6. Convert dictionary to JSON
student_json = json.dumps(student, indent=4)
print("Dictionary converted to JSON:")
print(student_json)
print("-" * 40)

# 7. Save JSON to file
with open("student_data.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON data saved to student_data.json")
print("-" * 40)

# 8. Read JSON back into Python
with open("student_data.json", "r") as file:
    student_from_file = json.load(file)

print("JSON read back into Python:")
print(student_from_file)
