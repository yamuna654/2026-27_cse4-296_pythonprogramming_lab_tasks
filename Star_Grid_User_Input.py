n = int(input("Enter grid size: "))
i = 1
while i <= n:
    for j in range(n):
        print("*", end=" ")
    print()
    i += 1