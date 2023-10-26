def remove_multiple_empty_strings(characters: list):
    list_string = []
    for string in characters:
        if string.strip():
            list_string.append(string)
    return list_string

