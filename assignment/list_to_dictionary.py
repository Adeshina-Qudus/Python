def list_to_dictionary(list_characters: list):
    dictionary = {}
    for count in list_characters:
        first_char = count[0].lower()
        if first_char in dictionary:
            first_char = count[0].upper()
        dictionary.update({first_char: count})
    return dictionary
