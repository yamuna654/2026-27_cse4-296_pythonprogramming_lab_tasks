def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_details(name="Yamuna", Python=90, Maths=85, English=88)