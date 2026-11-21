
n = int(input("Enter number of elements: "))

my_list = []

for i in range(n):
    element = int(input("Enter element: "))
    my_list.append(element)

print("List elements are:")

for element in my_list:
    print(element)
