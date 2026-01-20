# Demonstration of loops in Python with real-world examples
print("1. For loop: Print numbers from 1 to 100")
for i in range(1, 101):
    print(i, end=" ")
print("\n")

print("2. While loop: Countdown timer")
count = 10
while count > 0:
    print("Countdown:", count)
    count -= 1
print("Time's up!")
print("\n")

print("3. Break and Continue example")
for i in range(1, 11):
    if i == 5:
        print("Breaking the loop at", i)
        break
    if i == 3:
        continue
    print("Number:", i)
print("\n")

print("4. Iterating over string characters")
name = "Python"
for ch in name:
    print(ch)
print("\n")

print("5. Multiplication table of 5")
num = 5
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
print("\n")

print("6. Using range with steps (Even numbers from 2 to 20)")
for i in range(2, 21, 2):
    print(i, end=" ")
print("\n")


print("7. Loop with conditions (Check even or odd)")
for i in range(1, 11):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")
print("\n")

print("8. Real-world example: Checking shopping cart prices")
prices = [120, 340, 560, 80, 45]
total = 0
for price in prices:
    total += price
print("Total bill amount:", total)
print("\n")

print("9. Real-world example: Login attempts")
attempts = 3
while attempts > 0:
    print("Attempts left:", attempts)
    attempts -= 1
print("Account locked!")