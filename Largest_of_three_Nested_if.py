x = int(input("enter first number:"))
y = int(input("enter second number:"))
z = int(input("enter third number:"))
if x>y:
    if x>z:
        print(f"{x} is the largest number:")
    else:
        print(f"{z} is the largest number:")
else:
    if y>z:
        print(f"{y} is the largest number:")
    else:
        print(f"{z} is the largest number:")