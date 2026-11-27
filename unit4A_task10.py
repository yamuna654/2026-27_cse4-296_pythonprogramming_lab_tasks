students = [
    {"name": "Yamuna", "marks": 90},
    {"name": "meghana", "marks": 75},
    {"name": "loshimitha", "marks": 85},
    {"name": "prasanna", "marks": 95}
]
ascending = sorted(students, key=lambda x: x["marks"])
descending = sorted(students, key=lambda x: x["marks"], reverse=True)
print("Ascending Order:")
for student in ascending:
    print(student)

print("\nDescending Order:")
for student in descending:
    print(student)