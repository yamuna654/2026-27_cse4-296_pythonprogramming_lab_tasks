def totla_and_average(m1 , m2, m3):
    total =m1+ m2+ m3
    average = total/3
    return total, average
m1, m2, m3 = 70, 50, 80
total, average = totla_and_average(m1, m2, m3)
print(f"total: ", total )
print(f" average: ", average)