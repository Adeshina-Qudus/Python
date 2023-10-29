def frequency_element(numbers: list, givenValue: int):
    output_list = []
    for counter in numbers:
        counting = numbers.count(counter)
        if counting > givenValue:
            output_list.append(counter)
    return set(output_list)


