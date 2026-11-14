number = int(input("Enter a number between 1 and 100: "))
if ____:  # number is outside 1 to 100?
    print(f"{number} is not between 1 and 100")
elif ____:  # 1 is not prime
    print(f"{number} is not a prime number")
elif ____:  # number is 2, 3, 5, or 7?
    print(f"{number} is a prime number")
elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
    print(f"{number} is not a prime number")
else:
    print(f"{number} is a prime number")