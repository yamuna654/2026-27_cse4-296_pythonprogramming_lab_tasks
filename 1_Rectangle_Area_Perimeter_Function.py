def rectangle_area_perimeter(l,  b):
    area = l * b
    perimeter = 2 * (l + b)
    return area, perimeter

length = 5
breath = 3
area, perimeter = rectangle_area_perimeter(length, breath)
print(f"Area: {area}\nPerimeter: {perimeter}")
