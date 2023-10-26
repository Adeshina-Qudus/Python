list_number = [15, 20, 25, 20, 10, 5]
new_list = []
total = 0
for count in list_number:
    if count != list_number[3]:
        new_list.append(count)
print(new_list)
