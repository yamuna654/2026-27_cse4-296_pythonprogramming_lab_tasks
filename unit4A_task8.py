dict1 = {"Python": 90, "Maths": 85}
dict2 = {"Physics": 88, "English": 92}
merged_dict = dict1.copy()

merged_dict.update(dict2)
print("First Dictionary:", dict1)
print("Second Dictionary:", dict2)
print("Merged Dictionary:", merged_dict)