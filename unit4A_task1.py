student = {
    "name": "Yamuna",
    "age": 18,
    "course": "CSE"
}
print("Original Student Details:", student)

print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])

student["age"] = 19
student["city"] ="vijayawada"
print("Updated Student Details:", student)