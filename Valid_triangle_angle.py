angle1 = float(input("enter float angle1:"))
angle2 = float(input("enter float angle2:"))
angle3 = float(input("enter float angle3:"))
if angle1+angle2+angle3 == 180:
    print(f"The triangle with angles {angle1}, {angle2}, and {angle3} is valid.")
else:
    print(f"The triangle with angles {angle1}, {angle2}, and {angle3} is not valid.")