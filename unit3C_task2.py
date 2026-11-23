

numbers = {10, 20, 30, 40}

print("Original Set:", numbers)

print("Is 20 present?", 20 in numbers)
print("Is 50 present?", 50 in numbers)
numbers.add(50)
print("After Add:", numbers)
numbers.remove(20)
print("After Remove:", numbers)

numbers.discard(60)
print("After Discard:", numbers)