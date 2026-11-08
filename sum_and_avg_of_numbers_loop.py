n =int(input("enter how many numbers:"))
total = 0
for i in range(n):
    number = float(input("enter a number:"))
    total += number
average = total / n if n > 0 else 0
print(f"Sum: {total},\n Average: {average}")