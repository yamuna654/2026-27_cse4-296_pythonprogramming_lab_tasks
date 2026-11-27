students = {
    1: {"name": "Yamuna", "marks": 90},
    2: {"name": "Ravi", "marks": 85},
    3: {"name": "Sita", "marks": 95}
}
print("Student Details:")
for roll_no, details in students.items():
    print("Name:", details["name"])
    print("Marks:", details["marks"])