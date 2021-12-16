my_list = [22,44,55,1,2,5,4,88]

sorted_list = []

while my_list:
    minimum = my_list[0]

    for x in my_list:
        if x > minimum:
            minimum = x
    sorted_list.append(minimum)
    my_list.remove(minimum)

print(sorted_list)

