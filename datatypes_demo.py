# 1. Declaring variables of different data types
integer_var = 10            # int type
float_var = 3.5             # float type
string_var = "Hello Python" # string type
boolean_var = True          # boolean type

# 2. Printing the value and type of each variable
print("Integer Value:", integer_var, "| Type:", type(integer_var))
print("Float Value:", float_var, "| Type:", type(float_var))
print("String Value:", string_var, "| Type:", type(string_var))
print("Boolean Value:", boolean_var, "| Type:", type(boolean_var))

print("\n--- Arithmetic Operations ---")

# 3. Performing arithmetic operations using numeric variables
addition = integer_var + float_var
subtraction = integer_var - float_var
multiplication = integer_var * float_var
division = integer_var / float_var

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

print("\n--- Type Casting & Input Handling ---")

# 4. Taking user input (input is always string by default)
user_input = input("Enter a number: ")

try:
    # 5. Converting string input to integer
    int_value = int(user_input)
    print("Converted to Integer:", int_value)

    # 6. Converting string input to float
    float_value = float(user_input)
    print("Converted to Float:", float_value)

except ValueError:
    # 7. Handling invalid input using basic error handling
    print("Invalid input! Please enter a valid number.")

print("\n--- String Concatenation ---")

# 8. Concatenating string and number properly using type casting
age = 20
message = "My age is " + str(age)  # int converted to string before concatenation
print(message)

print("\n--- Dynamic Typing Demonstration ---")

# 9. Demonstrating dynamic typing by reassigning variable values
dynamic_var = 100
print("Value:", dynamic_var, "| Type:", type(dynamic_var))

dynamic_var = "Now I am a string"
print("Value:", dynamic_var, "| Type:", type(dynamic_var))

dynamic_var = False
print("Value:", dynamic_var, "| Type:", type(dynamic_var))
