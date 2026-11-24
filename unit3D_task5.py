def find_sum(*args):
    total = 0
    for num in args:
        total += num
    return total

result = find_sum(10, 20, 30, 40, 50)

print("Sum of values:", result)