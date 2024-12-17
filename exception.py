ls = [52, 43, 43, 55, 65, 78, 54, 47, 86, 45, 34, 64, 67]
try:
    choice = int(input("""Choose an option:
                         index of target item. 
                         value at a given position 
                         1 or 2:"""))
    if choice == 1:
        target = int(input("Enter your target item: "))
        if target in ls:
            index = ls.index(target)
            print("index of the target item is:" ,index)
        else:
            print("item not found ")
    elif choice == 2:
        position = int(input("Please enter a position: "))
        value = ls[position]
        print("value at position is:" ,value)
    else:
        print("error choice enter 1 or 2.")
except ValueError:
    print("error input Please enter a valid integer.")
except IndexError:
    print("error Position out of range ")
