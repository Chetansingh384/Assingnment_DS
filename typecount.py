items = [52, "hello", 41, 63.5, 96, "world", 85, 75.0, 48, 96.1, 93, 12, 5, "Python", 45, 74, 96.5, 85, 3, 22, 1, 23, 4]
string = 0
integer = 0
float = 0

for item in items:
    if type(item) == str:
        string += 1
    elif type(item) == int:
        integer += 1
    elif type(item) == float:
        float += 1
print("number of strings:", string)
print("number of integers:", integer)
print("number of floats:", float)

