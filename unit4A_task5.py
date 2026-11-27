marks = {
    "Python": 90,
    "Web Development": 85,
    "ctlr": 88,
    "English": 92,
}
print("Subject Names:")
for key in marks.keys():
    print(key)
print("\nSubject Marks:")
for value in marks.values():
    print(value)
print("\nSubject Names and Marks:")
for key, value in marks.items():
    print(key, ":", value)