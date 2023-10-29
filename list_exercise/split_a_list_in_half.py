sample_input = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
two_list = [[],[]]
for index, value in enumerate(sample_input):
    if index < 5:
        two_list[0].append(value)
    if index >= 5:
        two_list[1].append(value)
print(two_list)
