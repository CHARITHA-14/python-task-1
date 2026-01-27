import csv

# ---------- TEXT FILE OPERATIONS ----------

try:
    # 1. Create text file and 2. Write user data into file
    with open("data.txt", "w") as file:
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")

    print("Data written to file successfully.\n")

    # 3. Read file contents
    print("Reading file contents:")
    with open("data.txt", "r") as file:
        print(file.read())

    # 4. Append data to file
    with open("data.txt", "a") as file:
        file.write("Status: Active\n")

    print("Data appended successfully.\n")

except FileNotFoundError:
    print("File not found error occurred.")
except IOError:
    print("Input/Output error occurred.")

# ---------- CSV FILE OPERATIONS ----------

try:
    # 6. Create CSV file using csv module and 7. Write multiple rows
    with open("data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["ID", "Name", "Marks"])
        writer.writerow([1, "Charitha", 85])
        writer.writerow([2, "Anjali", 90])
        writer.writerow([3, "Rahul", 88])

    print("CSV file written successfully.\n")

    # 8. Read CSV data
    print("Reading CSV file contents:")
    with open("data.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

except Exception as e:
    print("An error occurred:", e)

