ls = [52, 41, 63, 96, 85, 75, 48, 96, 93, 12, 5, 45, 74, 96, 85, 3, 22, 1, 23, 4]
min = ls[0]
max = ls[0]
for item in ls:
    if item < min:
        min = item
    if item > max:
        max = item
print("Minimum value:", min)
print("Maximum value:", max)
